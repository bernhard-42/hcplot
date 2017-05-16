# Copyright 2017 Bernhard Walter
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pandas as pd
import numpy as np
import itertools
from functools import reduce

# TODO: Add Spark DataFrame

class GroupedData(object):

    def __init__(self, data, colDims=[], rowDims=[]):
        assert isinstance(data, (dict, pd.DataFrame)), "Data must be eiter ColumnDataList or a Pandas DataFrame"
        
        self.colDims = colDims
        self.rowDims = rowDims
        self.allDims = colDims + rowDims
        self.multiIndex = len(self.allDims) > 1
        self.noIndex = len(self.allDims) == 0
        
        self.df = data.copy() if isinstance(data, pd.DataFrame) else pd.DataFrame(data)
        self.levels = {}
        
        self.colLevels = self.rowLevels = []
        
        if not self.noIndex:
            self.df, self.levels, self.colLevels, self.rowLevels = self._indexData()
            self.colLevels, self.rowLevels = self._createLevels()

        self.colCount = len(self.colLevels)
        self.rowCount = len(self.rowLevels)

        self.minMax = {}
    
    
    def _indexData(self):
        df = self.df.set_index(self.allDims)
        df.sortlevel(inplace=True)
        if self.multiIndex:
            levels = [x.tolist() for x in df.index.unique().levels]
        else:
            levels = [sorted(df.index.unique().tolist())]
        return df, levels, levels[:len(self.colDims)], levels[len(self.colDims):]

    
    def _createLevels(self):
        result = []
        for levels in [self.colLevels, self.rowLevels]:
            if len(levels) == 1:
                result.append([(l,) for l in levels[0]])
            else:
                result.append(list(itertools.product(*levels)))
        return result

    
    def _getLabels(self, dims, levels, func):
        if func is None:
            func = lambda k,v: "%s : %s" % (k,v)
        if len(dims) == 0:
            return []
        else:
            return [[func(k,v) for k,v in zip(dims, val)] for val in levels]

        
    def getRowLabels(self, func=None):
        return self._getLabels(self.rowDims, self.rowLevels, func)

    
    def getColLabels(self, func=None):
        return self._getLabels(self.colDims, self.colLevels, func)
    
    
    def getShape(self):
        return (self.rowCount, self.colCount)

        
    def getMinMax(self, col):
        if self.minMax.get(col) is None:
            self.minMax[col] = (self.df[col].min(), self.df[col].max())
        return self.minMax[col]
    
    
    def getLevelsByIndex(self, colIndex, rowIndex=None):
        levels = []
        if colIndex is not None:
            levels += self.colLevels[colIndex]
        if rowIndex is not None:
            levels += self.rowLevels[rowIndex]            
        return levels


    def getDataByIndex(self, colIndex, rowIndex=None):
        levels = self.getLevelsByIndex(colIndex, rowIndex)   
        if self.noIndex:
            return self.df
        elif self.multiIndex:
            return self.df.xs(levels, level=self.allDims)
        else:
            return self.df.loc[levels[0]]
