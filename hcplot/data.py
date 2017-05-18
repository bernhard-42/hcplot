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

labelFomatter = lambda k,v: "%s : %s" % (k,v)

class Data(object):

    def __init__(self, data):
        self.df = data.copy() if isinstance(data, pd.DataFrame) else pd.DataFrame(data)
        self.minMax = {}
        
    def getData(self):
        return self.df

    def getMinMax(self, col):
        if self.minMax.get(col) is None:
            self.minMax[col] = (self.df[col].min(), self.df[col].max())
        return self.minMax[col]
    

class WrapData(Data):

    def __init__(self, data, colDims):
        assert isinstance(data, (dict, pd.DataFrame)), "Data must be eiter ColumnDataList or a Pandas DataFrame"
        super(__class__, self).__init__(data)

        self.colDims = colDims
        self.colCategories = []

        self._prepareData()


    def _prepareData(self):
        self.allDims = self.colDims

        self.df, self.levels = self._indexData()
        self.colLevels = self.levels

        self.colCategories = self._createCategories([self.colLevels])[0]
        self.colCount = len(self.colCategories)
        self.rowCount = 0
 
    
    def _indexData(self):
        self.multiIndex = len(self.allDims) > 1
        df = self.df.set_index(self.allDims)
        df.sortlevel(inplace=True)

        if self.multiIndex:
            levels = [level.tolist() for level in df.index.unique().levels]
        else:
            levels = [sorted(df.index.unique().tolist())]

        return df, levels

    
    def _createCategories(self, allLevels):
        result = []
        for levels in allLevels:
            if len(levels) == 1:
                result.append([(l,) for l in levels[0]])
            else:
                result.append(list(itertools.product(*levels)))
        return result

    
    def _getLabels(self, dims, categories, func=labelFomatter):
        return [[func(k,v) for k,v in zip(dims, val)] for val in categories]

        
    def getColLabels(self, func=labelFomatter):
        return self._getLabels(self.colDims, self.colCategories, func)
    
    
    def getShape(self):
        return (self.rowCount, self.colCount)

        
    def getCategories(self, colIndex):
        return self.colCategories[colIndex]


    def getData(self, colIndex):
        categories = self.getCategories(colIndex)
        if self.multiIndex:
            return self.df.xs(categories, level=self.allDims)
        else:
            return self.df.loc[categories[0]]



class GridData(WrapData):

    def __init__(self, data, colDims, rowDims):
        assert isinstance(data, (dict, pd.DataFrame)), "Data must be eiter ColumnDataList or a Pandas DataFrame"

        self.rowDims = rowDims
        self.rowCategories = []
        super(__class__, self).__init__(data, colDims)

    def _prepareData(self):
        self.allDims = self.colDims + self.rowDims

        self.df, self.levels = self._indexData()
        self.colLevels = self.levels[:len(self.colDims)]
        self.rowLevels = self.levels[len(self.colDims):]

        self.colCategories, self.rowCategories = self._createCategories([self.colLevels, self.rowLevels])

        self.colCount = len(self.colCategories)
        self.rowCount = len(self.rowCategories)


    def getRowLabels(self, func=labelFomatter):
        return self._getLabels(self.rowDims, self.rowCategories, func)

    
    def getCategories(self, colIndex, rowIndex):
        return self.colCategories[colIndex] + self.rowCategories[rowIndex]  


    def getData(self, colIndex, rowIndex):
        categories = self.getCategories(colIndex, rowIndex)   
        if self.multiIndex:
            return self.df.xs(categories, level=self.allDims)
        else:
            return self.df.loc[categories[0]]
