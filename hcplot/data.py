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

    def __init__(self, data, rowDims=None, colDims=None):
        
        self.df = None
        if isinstance(data, dict):
            self.df = pd.DataFrame(data)
        elif isinstance(data, pd.DataFrame):
            self.df = data

        self.rowDims = rowDims
        self.colDims = colDims

        self.rowCategories = []
        self.rowCount = None
        if rowDims is not None:
            self.rowCategories = self.explodeCategories(rowDims)
            self.rowCount = len(self.rowCategories)

        self.colCategories = []
        self.colCount = None
        if colDims is not None:
            self.colCategories = self.explodeCategories(colDims)
            self.colCount = len(self.colCategories)

        self.minMax = {}


    def getMinMax(self, col):
        if self.minMax.get(col) is None:
            self.minMax[col] = (self.df[col].min(), self.df[col].max())
        return self.minMax[col]


    def explodeCategories(self, dims):
        categoryValues = [ sorted(self.df.groupby(dim).groups.keys()) for dim in dims ]
        categories =     [ list(zip(dims, cats)) for cats in itertools.product(*categoryValues) ]
        return categories


    def getShape(self):
        return (1 if self.rowCount is None else self.rowCount,
                1 if self.colCount is None else self.colCount)

    
    def getCategoriesByIndex(self, rowIndex=None, colIndex=None):
        if rowIndex is not None and colIndex is not None:
            return (self.rowCategories[rowIndex], self.colCategories[colIndex])
        
        elif rowIndex is not None:
            return self.rowCategories[rowIndex]
        
        elif colIndex is not None:
            return self.colCategories[colIndex]
        
        else:
            raise ValueError("Access type unknown")

        
    def getDataByIndex(self, rowIndex=None, colIndex=None):

        def makeDict(data, row=False, col=False):
            return {"rowCategories": self.rowCategories[rowIndex] if row else {}, 
                    "colCategories": self.colCategories[colIndex] if col else {},
                    "data": data}
        
        if rowIndex == 0 and colIndex == 0 and \
           self.rowCount is None and self.colCount is None:                   # layout type single, matrix
            return makeDict(self.df)
        
        elif rowIndex is not None and colIndex is not None and \
           self.rowCount is not None and self.colCount is not None:           # layout type grid
            index = self.rowCategories[rowIndex] + self.colCategories[colIndex]
            return makeDict(self.getDataByCategories(index), row=True, col=True)
        
        elif colIndex is not None and self.colCount is not None:               # layout type wrap
            return makeDict(self.getDataByCategories(self.colCategories[colIndex]), col=True)
        
        else:
            return makeDict(self.df)


    def getDataByCategories(self, categories):
        cond = reduce(np.logical_and, [self.df[cat[0]] == cat[1] for cat in categories])
        return self.df[cond]
  
    
    def getRowLabels(self):
        if self.rowCount == 0:
            return []
        else:
            return [["%s : %s" % (val[0], val[1]) for val in vals] for vals in self.rowCategories]


    def getColLabels(self):
        if self.colCount == 0:
            return []
        else:
            return [["%s : %s" % (val[0], val[1]) for val in vals] for vals in self.colCategories]
