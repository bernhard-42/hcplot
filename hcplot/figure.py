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
from .utils import ScipyEncoder, single
from .components import Components
from .templates import createGrid, createWrap

from IPython.display import Javascript, HTML, display
from uuid import uuid4
from textwrap import dedent
import math
import json
from operator import itemgetter


class Figure(object):
    
    def __init__(self, data, mapping, layout=None, coord=None, scaleX=None, scaleY=None, width=1024, ratio=2/3):
        self.id = str(uuid4())
        self.rawData = data

        self.mapping = mapping        
        self.layout = single() if layout is None else layout

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
            assert  isinstance(self.mapping["x"], str), "'x' has to be a column name"
            assert  isinstance(self.mapping["y"], str), "'y' has to be a column name"

            self.data = GroupedData(data, rowDims=self.layout.get("x"), colDims=self.layout.get("y"))
            self.rows = self.data.getShape()[0]
            self.cols = self.data.getShape()[1]
            self.count = self.rows * self.cols

        elif layoutType == "matrix":
            if self.mapping["y"] is None:
                self.mapping["y"] = self.mapping["x"].copy()
                self.mapping["y"].reverse()
                
            assert  isinstance(self.mapping["x"], (list, tuple)), "'x' has to be a list of column names [..., ]"
            assert  isinstance(self.mapping["y"], (list, tuple)), "'y' has to be a list of column names [..., ]"

            self.data = GroupedData(data)
            self.rows = len(self.mapping.get("x"))
            self.cols = len(self.mapping.get("y"))
            self.count = self.rows * self.cols

        else:
            raise ValueError("Unknow layout type %s", layoutType)

        self.coord = coord
        self.scaleX = scaleX
        self.scaleY = scaleY
        
        self.width = width
        self.ratio = ratio

        self.layers = []


    def __add__(self, layers):
        layers.setFigure(self)
        self.layers.append(layers)
        return self


    def createContainer(self):
        labelHeight = self.layout.get("labelHeight", 20)

        layoutType = self.layout.get("type")
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
                                      colLabels, labelHeight)
                else:
                    html = createGrid(self.id, self.width, self.ratio, self.rows, self.cols,
                                      rowLabels, colLabels, labelHeight)
            else:
                html = createGrid(self.id, self.width, self.ratio, self.rows, self.cols)
        
        else:
            raise NotImplementedError("Not implemented yet")

        return html

    
    def getDataSlice(self, row, col, mx, my):
        df = self.data.getDataByIndex(row, col)["data"]
        if mx == my:
            return [[val[0], val[0]] for val in df[[mx]].to_dict("split")["data"]]
        else:
            return df[[mx, my]].to_dict("split")["data"]


    def createChart(self):

        layoutType = self.layout.get("type")
        html = self.createContainer()

        html += dedent("""
        <script>
            window.hc_charts.promise.then(function(HC) {
        """)
        
        if layoutType == "matrix":
            allCols = list(set(self.mapping["x"]).union(set(self.mapping["y"])))
            minMax = [self.data.getMinMax(col) for col in allCols]
            xmin = ymin = min(minMax, key=itemgetter(0))[0]
            xmax = ymax = max(minMax, key=itemgetter(1))[1]
        else:
            xmin, xmax = self.data.getMinMax(self.mapping["x"])
            ymin, ymax = self.data.getMinMax(self.mapping["y"])

        i = 0

        for row in range(self.rows):
            for col in range(self.cols):

                fig = Components().figure(zoomType="xy", exporting=False, title=None, legend=False)

                if col == 0:
                    fig.updateChart(marginLeft=50,   width=self.width//self.cols+40)
                if row == self.rows-1:
                    fig.updateChart(marginBottom=40, height=(self.width//self.cols)*self.ratio+30)

                if True:
                    fig.addXAxis(title=None, max=xmax, min=xmin, lineWidth=1, tickWidth=1, gridLineWidth=1)
                    fig.addYAxis(title=None, max=ymax, min=ymin, lineWidth=1, tickWidth=1, gridLineWidth=1)
                else:
                    fig.addXAxis(title=None, lineWidth=1, tickWidth=1, gridLineWidth=1)
                    fig.addYAxis(title=None, lineWidth=1, tickWidth=1, gridLineWidth=1)
                    
                if col != 0:
                    fig.updateYAxis(labels=False)
                                    
                if row != self.rows - 1 and layoutType != "wrap":
                    fig.updateXAxis(labels=False)
                
                if i != self.count - 1:
                    fig.updateFigure(credits=False)

                if i < self.count:
                    for layer in self.layers:
                        mx, my = self.mapping["x"], self.mapping["y"]

                        if layoutType == "single":
                            data = self.getDataSlice(None, None, mx, my)
                            
                        elif layoutType == "wrap":
                            data = self.getDataSlice(0, i, mx, my)
                            
                        elif layoutType == "grid":
                            data = self.getDataSlice(row, col, mx, my)
                            
                        elif layoutType == "matrix":
                            mx = mx[col]
                            my = my[row]
                            data = self.getDataSlice(None, None, mx, my)
                            
                        # TODO: clean to use layer data if exists
                        fig.addSeries(my, data, layer.options)

                    container = "hc_%s_%d-%d" % (self.id, row, col)
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

