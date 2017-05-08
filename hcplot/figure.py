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

from IPython.display import Javascript, HTML, display
from .data import GroupedData
from .utils import ScipyEncoder
from uuid import uuid4
from textwrap import dedent
import math
import json


class Figure(object):
    
    def __init__(self, data, mapping, layout=None, coord=None, scaleX=None, scaleY=None):
        self.id = str(uuid4())
        self.rawData = data
        if layout is None:
            self.data = GroupedData(data)
        else:
            self.data = GroupedData(data, rowDims=layout.get("x"), colDims=layout.get("y"))
        self.mapping = mapping
        self.layout = layout
        self.coord = coord
        self.scaleX = scaleX
        self.scaleY = scaleY
        
        if self.layout is None:
            rows = cols = 1
            count = 1
        elif self.layout["type"] == "float":
            divCeil = lambda x,y : (x // y) + (1 if (x % y) > 0 else 0)
            count = self.data.getShape()[0]
            if self.layout.get("nrows") is not None:
                rows = self.layout["nrows"]
                cols = divCeil(count, layout["nrows"])
            elif layout.get("ncols") is not None:
                rows = divCeil(count, layout["ncols"])
                cols = self.layout["ncols"]
        else:
            rows = self.data.getShape()[0]
            cols = self.data.getShape()[1]
            count = rows * cols
        self.rows = rows
        self.cols = cols
        self.count = count
        
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
        
        # TODO: trash this
        def createLabel(x):
            return " : ".join([(str(k),str(v)) for k,v in list(x.items())][0])
        
        i = 0
        space = 10
        width = (1024 // self.cols) - space
        height = width # (width * 2) // 3
        
        html = """<div id="hc_%s">\n""" % self.id
        for row in range(self.rows):
            html += """  <div id="hc_%s_%d">\n""" % (self.id, row)
            for col in range(self.cols):
                # TDOD: calculate clorrect offsets
                w = width +  30 if col == 0 else width
                h = height + 20 if row == self.rows-1 else height
                style = """ style="display:inline-block; width:%dpx; height:%dpx" """ % (w, h)
                if i < self.count:
                    html += """    <div id="hc_%s_%d-%d" %s></div>\n""" % \
                            (self.id, row, col, style)
                i += 1
            html += "  </div>\n"
        html += "</div>\n"
    
        html += dedent("""
        <script>
            window.hc_charts.promise.then(function(HC) {
        """)

        xmin, xmax = createRange("x")
        ymin, ymax = createRange("y")

        i = 0
        for row in range(self.rows):
            for col in range(self.cols):
                figure = {
                    "chart":  { "zoomType": 'xy' },
                    "exporting": { "enabled": False },
                    "title":  {"text": None},
                    "legend": {"enabled": False},
                    "xAxis":  {
                        "title": {"text": None if self.layout is None else createLabel(self.data.colCategories[col])},
                        "lineWidth": 1,
                        "tickWidth": 1,
                        "gridLineWidth": 1,
                        "min": xmin, "max":xmax
                    },
                    "yAxis": {
                        "title": {"text": None if self.layout is None else createLabel(self.data.rowCategories[row])},
                        "lineWidth": 1,
                        "tickWidth": 1,
                        "minorGridLineWidth": 1,
                        "min": ymin, "max":ymax
                    },
                    "series": []
                }
                
                if col != 0:
                    figure["yAxis"].update({
                        "title": {"text": None},
                        "labels": {"enabled": False },
                    })
                    
                
                if row != self.rows - 1:
                    figure["xAxis"].update({
                        "title": {"text": None},
                        "labels": {"enabled": False },
                    })
                
                if i != self.count - 1:
                    figure["credits"] = False

                if i < self.count:
                    for layer in self.layers:
                        data = self.data.getDataByIndex(row, col)["data"][[self.mapping["x"], self.mapping["y"]]]
                        # TODO: clean to use layer data if exists
                        series = {
                                  "name": self.mapping["y"], 
                                  "data": data.to_dict("split")["data"]
                                 }
                        series.update(layer.options)
                        figure["series"].append(series)

                    container = "hc_%s_%d-%d" % (self.id, row, col)
                    html += dedent("""
                    //      CHART %d-%d
                            HC.chart("%s", %s);
                    """) % (row, col, container, json.dumps(figure, cls=ScipyEncoder))
                    i += 1

        html += dedent("""
            });
        </script>
        """)

        return html


    def _repr_html_(self):
        return self.createChart()
