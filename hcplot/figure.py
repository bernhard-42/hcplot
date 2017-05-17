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

from .data import GroupedData
from .utils import ScipyEncoder, update, Config
from .scale import defaultScale
from .components import Components
from .templates import createGrid, createWrap

from IPython.display import Javascript, HTML, display
from uuid import uuid4
from textwrap import dedent
import math
import json
from operator import itemgetter


class Figure(object):
    
    def __init__(self, data,                                          # DataFrame or ColumnDataSource
                 *args,                                               # Config objects
                 width=1024, ratio=2/3, performanceTreshold=1000):    # global attributes

        self.id = str(uuid4())
        self.layer = 0
        self.layers = []
        
        self.width = width
        self.ratio = ratio
        self.performanceTreshold = performanceTreshold
       
        # define all possible configs, ...
        self.mapping = {}
        self.layout  = {"type": "single", "labels": True}
        self.scales  = defaultScale()
        self.coord   = {} # TODO
        
        # ... get all provided configs ...
        for arg in args:
            assert isinstance(arg, Config), "Only Config objects allowed as positional arguments"
            getattr(self, arg.param).update(arg.config)

        assert self.mapping is not None, "Mapping Config (with at least x column) is missing"

        self._indexData(data)
        
        self.coding = self.createPlotConfig(self.mapping, self.scales, self.layer)
        self.usePlotLevel = {col:"%s._0" % col for col in self.mapping.keys() if col not in ["x", "y"]}

    
    def _indexData(self, data):
        layoutType = self.layout.get("type")
        
        if layoutType == "single":
            self.data = GroupedData(data)
            self.count = 1
            self.rows = 1
            self.cols = 1

        elif layoutType == "wrap":
            nrows = self.layout.get("nrows")
            ncols = self.layout.get("ncols")

            assert nrows is None or ncols is None, "Set either nrows or ncols in wrap layout"

            if nrows is None and ncols is None:
                nrows = 1

            self.data = GroupedData(data, colDims=self.layout.get("y"))
            self.count = self.data.getShape()[1]

            if ncols is None:
                self.rows = nrows
                self.cols = math.ceil(self.count / nrows)
            elif nrows is None:
                self.rows = math.ceil(self.count / ncols)
                self.cols = ncols

        elif layoutType == "grid":
            assert  isinstance(self.mapping.get("x"), str), "'x' has to be a column name"
            assert  isinstance(self.mapping.get("y"), str), "'y' has to be a column name"

            self.data = GroupedData(data, rowDims=self.layout.get("x"), colDims=self.layout.get("y"))
            self.rows = self.data.getShape()[0]
            self.cols = self.data.getShape()[1]
            self.count = self.rows * self.cols

        elif layoutType == "matrix":
            if self.mapping.get("y") is None:
                self.mapping["y"] = self.mapping["x"].copy()
                self.mapping["y"].reverse()
                
            assert  isinstance(self.mapping["x"], (list, tuple)), "'x' has to be a list of column names [..., ]"
            assert  isinstance(self.mapping["y"], (list, tuple)), "'y' has to be a list of column names [..., ]"

            self.data = GroupedData(data)
            self.cols = len(self.mapping.get("x"))
            self.rows = len(self.mapping.get("y"))
            self.count = self.rows * self.cols

        else:
            raise ValueError("Unknow layout type %s", layoutType)

    
    def createPlotConfig(self, mapping, scales, layer):
        coding = {}
        for attr, name in mapping.items():
            layerAttr = "%s._%d" % (attr, layer)
            if name is not None and attr not in ["x", "y"] and scales.get(attr) is not None:
                df = self.data.df
                df[layerAttr] = df[name].astype("category")
                count = df[layerAttr].cat.categories.size
                newValues = scales[attr](count)
                coding[attr] = zip(df[layerAttr].cat.categories, newValues)
                df[layerAttr] = df[layerAttr].cat.rename_categories(newValues)
        return coding
    
    def __add__(self, layers):
        layers.setFigure(self)
        self.layers.append(layers)
        return self


    def createContainer(self, layoutType, xScaleFree, yScaleFree, labelHeight):
        if layoutType == "single":
            html = createGrid(self.id, self.width, self.ratio, 1, 1)
                
        elif layoutType in ["grid", "wrap", "matrix"]:
            
            if self.layout.get("labels"):
                if layoutType == "matrix":
                    rowLabels = [["y = %s" % el] for el in self.mapping.get("y")]
                    colLabels = [["x = %s" % el] for el in self.mapping.get("x")]
                else:
                    rowLabels = self.data.getRowLabels() if layoutType == "grid" else []
                    colLabels = self.data.getColLabels()

                if layoutType == "wrap":
                    html = createWrap(self.id, self.width, self.ratio, self.rows, self.cols, self.count,
                                      colLabels, labelHeight, allYAxisLabels=yScaleFree)
                else:
                    html = createGrid(self.id, self.width, self.ratio, self.rows, self.cols,
                                      rowLabels, colLabels, labelHeight, 
                                      allXAxisLabels=xScaleFree, allYAxisLabels=yScaleFree)
            else:
                html = createGrid(self.id, self.width, self.ratio, self.rows, self.cols, 
                                  allXAxisLabels=xScaleFree, allYAxisLabels=yScaleFree)
        
        else:
            raise NotImplementedError("Not implemented yet")

        return html

    
    def getDataSlice(self, row, col):
        return self.data.getDataByIndex(col, row)

    
    def getMinMax(self, layoutType, xScaleFree, yScaleFree):
        xmin = ymin = xmax = ymax = None
        if not (xScaleFree and yScaleFree):
            if layoutType == "matrix":
                allCols = list(set(self.mapping["x"]).union(set(self.mapping["y"])))
                minMax = [self.data.getMinMax(col) for col in allCols]
                if not xScaleFree:
                    xmin = ymin = min(minMax, key=itemgetter(0))[0]
                if not yScaleFree:
                    xmax = ymax = max(minMax, key=itemgetter(1))[1]
            else:
                if not xScaleFree:
                    xmin, xmax = self.data.getMinMax(self.mapping["x"])
                if not yScaleFree:
                    ymin, ymax = self.data.getMinMax(self.mapping["y"])
        return xmin, ymin, xmax, ymax


    def createChart(self):

        layoutType = self.layout.get("type", "single")
        scaleType  = self.layout.get("scales", "fixed")
        labelHeight = self.layout.get("labelHeight", 20)

        xScaleFree = (scaleType in ["free", "free_x"]) # if layoutType != "wrap" else True
        yScaleFree = (scaleType in ["free", "free_y"])

        xmin, ymin, xmax, ymax = self.getMinMax(layoutType, xScaleFree, yScaleFree)

        html = self.createContainer(layoutType, xScaleFree, yScaleFree, labelHeight)

        html += dedent("""
        <script>
            window.hc_charts.promise.then(function(HC) {
        """)

        i = 0

        for row in range(self.rows):
            for col in range(self.cols):

                fig = Components().figure(zoomType="xy", exporting=False, title=None, legend=False)

                fig.addXAxis(title=None, max=xmax, min=xmin, lineWidth=1, tickWidth=1, gridLineWidth=1)
                fig.addYAxis(title=None, max=ymax, min=ymin, lineWidth=1, tickWidth=1, gridLineWidth=1)
                    
                if xScaleFree or row == self.rows - 1 or layoutType == "wrap":
                    fig.updateChart(marginBottom=40, height=(self.width//self.cols)*self.ratio+30)
                else:
                    fig.updateXAxis(labels=False)
                
                if yScaleFree or col == 0:
                    fig.updateChart(marginLeft=50,   width=self.width//self.cols+40)
                else:
                    fig.updateYAxis(labels=False)

                if i != self.count - 1:
                    fig.updateFigure(credits=False)

                if i < self.count:
                    mx, my = self.mapping["x"], self.mapping["y"]

                    if layoutType == "single":
                        data = self.getDataSlice(None, None)

                    elif layoutType == "wrap":
                        data = self.getDataSlice(0, i)

                    elif layoutType == "grid":
                        data = self.getDataSlice(row, col)

                    elif layoutType == "matrix":
                        mx = mx[col]
                        my = my[row]
                        data = self.getDataSlice(None, None)

                    isEmpty = not (len(data) > 0)
                    for layer in self.layers:
                        data = layer.prepareData(data, mx, my)
                        fig.addSeries(my, data, layer.options)

                    container = "hc_%s_%d-%d" % (self.id, row, col)
                    if isEmpty and xScaleFree and yScaleFree:
                        html += dedent("""
                        //      console.log("%d-%d")
                        """) % (row, col)
                    else:
                        html += dedent("""
                        //      console.log("%d-%d")
                                HC.chart("%s", %s);
                        """) % (row, col, container, json.dumps(fig.get(), cls=ScipyEncoder))

                    i += 1

        html += dedent("""
            });
        </script>
        """)

        return html
    
    
    def _repr_html_(self):
        return self.createChart()
