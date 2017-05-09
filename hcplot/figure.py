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
from .templates import createGrid

from IPython.display import Javascript, HTML, display
from uuid import uuid4
from textwrap import dedent
import math
import json


class Figure(object):
    
    def __init__(self, data, mapping, layout=None, coord=None, scaleX=None, scaleY=None):
        self.id = str(uuid4())
        self.rawData = data
        if layout is None:
            self.layout = single()
            self.data = GroupedData(data)
        else:
            self.layout = layout
            self.data = GroupedData(data, rowDims=layout.get("x"), colDims=layout.get("y"))
        
        self.mapping = mapping
        
        self.coord = coord
        self.scaleX = scaleX
        self.scaleY = scaleY
        
        if self.layout == {}:
            self.rows = self.cols = 1
            self.count = 1
        elif self.layout.get("type") == "float":
            divCeil = lambda x,y : (x // y) + (1 if (x % y) > 0 else 0)
            self.count = self.data.getShape()[0]
            if self.layout.get("nrows") is not None:
                self.rows = self.layout["nrows"]
                self.cols = divCeil(count, layout["nrows"])
            elif layout.get("ncols") is not None:
                self.rows = divCeil(count, layout["ncols"])
                self.cols = self.layout["ncols"]
        else:
            self.rows = self.data.getShape()[0]
            self.cols = self.data.getShape()[1]
            self.count = self.rows * self.cols
        
        self.layers = []


    def __add__(self, layers):
        layers.setFigure(self)
        self.layers.append(layers)
        return self


    def createChart(self):

        # TODO: trash this
        def createRange(ax):
            axmin = self.rawData[self.mapping[ax]].min() 
            axmax = self.rawData[self.mapping[ax]].max() 
            if axmax - axmin > 5:
                axmin = math.floor(axmin / 5) * 5
                axmax = math.ceil(axmax / 5) * 5
            elif axmax - axmin > 2:
                axmin = math.floor(axmin / 2) * 2
                axmax = math.ceil(axmax / 2) * 2
            return axmin, axmax

        
        width = self.layout.get("width", 1024)
        ratio = self.layout.get("ratio", 0.66)
        labelHeight = 20

        if self.layout.get("type") == "grid":
            if self.layout.get("labels"):
                rowLabels = self.data.getRowLabels()
                colLabels = self.data.getColLabels()
                html = createGrid(self.id, width, ratio, self.rows, self.cols, rowLabels, colLabels, labelHeight)
            else:
                html = createGrid(self.id, width, ratio, self.rows, self.cols)

        elif self.layout.get("type") == "single":
            html = createGrid(self.id, width, ratio, 1, 1)
        else:
            print("Not implemented yet")
            return

        html += dedent("""
        <script>
            window.hc_charts.promise.then(function(HC) {
        """)

        xmin, xmax = createRange("x")
        ymin, ymax = createRange("y")

        i = 0
        for row in range(self.rows):
            for col in range(self.cols):
                fig = Components().figure(zoomType="xy", exporting=False, title=None, legend=False)

                if col == 0:
                    fig.updateChart(marginLeft=50,   width=width//self.cols+40)
                if row == self.rows-1:
                    fig.updateChart(marginBottom=40, height=(width//self.cols)*ratio+30)

                fig.addXAxis(title=None, max=xmax, min=xmin, lineWidth=1, tickWidth=1, gridLineWidth=1)
                fig.addYAxis(title=None, max=ymax, min=ymin, lineWidth=1, tickWidth=1, gridLineWidth=1)
                
                if col != 0:
                    fig.updateYAxis(labels=False)
                                    
                if row != self.rows - 1:
                    fig.updateXAxis(labels=False)
                
                if i != self.count - 1:
                    fig.updateFigure(credits = False)

                if i < self.count:
                    for layer in self.layers:
                        data = self.data.getDataByIndex(row, col)["data"][[self.mapping["x"], self.mapping["y"]]]
                        # TODO: clean to use layer data if exists
                        fig.addSeries(self.mapping["y"], data.to_dict("split")["data"], layer.options)

                    container = "hc_%s_%d-%d" % (self.id, row, col)
                    html += dedent("""
                    //      CHART %d-%d
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
