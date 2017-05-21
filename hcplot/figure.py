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

from .data import Data, WrapData, GridData
from .base import Base
from .utils.json import ScipyEncoder
from .scales.scale import defaultScale
from .components import Components
from .templates import createGrid, createWrap

from uuid import uuid4
from textwrap import dedent
import math
import json


class Figure(Base):

    def __init__(self, *dataOrConfigs,   # DataFrame or ColumnDataSource (data)or Config objects
                 width=1024, ratio=0.618, performanceTreshold=1000):    # global attributes

        self.id = str(uuid4())
        self.layer = 0
        self.rows = self.cols = self.count = 1
        self.layers = []

        self.xmin = self.ymin = self.xmax = self.ymax = None

        self.width = width
        self.ratio = ratio
        self.performanceTreshold = performanceTreshold
        self.usePlotLevel = {}

        self.layout = {"type": "single", "labels": True}
        self.coord = {}  # TODO

        # define all possible configs, ...
        self.mapping = {}
        self.scales = defaultScale()

        data = self.parseArgs(dataOrConfigs)

        if data is not None:
            self._indexData(data)

            self.coding = self.createPlotConfig(self.mapping, self.scales, self.layer)
            self.usePlotLevel = {}
            for k, v in self.coding.items():
                if k not in ["x", "y"]:
                    self.usePlotLevel[k] = v if isinstance(v, str) else "%s._0" % k

    def _indexData(self, data):
        layoutType = self.layout.get("type")

        if layoutType == "single":
            self.data = Data(data)
            self.count = 1
            self.rows = 1
            self.cols = 1

        elif layoutType == "wrap":
            nrows = self.layout.get("nrows")
            ncols = self.layout.get("ncols")

            assert nrows is None or ncols is None, "Set either nrows or ncols in wrap layout"

            if nrows is None and ncols is None:
                nrows = 1

            self.data = WrapData(data, self.layout.get("y"))
            self.count = self.data.getShape()[1]

            if ncols is None:
                self.rows = nrows
                self.cols = math.ceil(self.count / nrows)
            elif nrows is None:
                self.rows = math.ceil(self.count / ncols)
                self.cols = ncols

        elif layoutType == "grid":
            assert isinstance(self.mapping.get("x"), str), "'x' has to be a column name"
            assert isinstance(self.mapping.get("y"), str), "'y' has to be a column name"

            self.data = GridData(data, self.layout.get("y"), self.layout.get("x"))
            self.rows = self.data.getShape()[0]
            self.cols = self.data.getShape()[1]
            self.count = self.rows * self.cols

        elif layoutType == "matrix":
            if self.mapping.get("y") is None:
                self.mapping["y"] = self.mapping["x"].copy()
                self.mapping["y"].reverse()

            assert isinstance(self.mapping["x"], (list, tuple)), \
                "'x' has to be a list of column names [..., ]"
            assert isinstance(self.mapping["y"], (list, tuple)), \
                "'y' has to be a list of column names [..., ]"

            self.data = Data(data)
            self.cols = len(self.mapping.get("x"))
            self.rows = len(self.mapping.get("y"))
            self.count = self.rows * self.cols

        else:
            raise ValueError("Unknow layout type %s", layoutType)

    def _setMinMax(self, xmin, ymin, xmax, ymax):
        def cmp(o, n, f):
            if n is None:
                return o
            else:
                return n if o is None else f(o, n)

        self.xmin = cmp(xmin, self.xmin, min)
        self.ymin = cmp(ymin, self.ymin, min)
        self.xmax = cmp(xmax, self.xmax, max)
        self.ymax = cmp(ymax, self.ymax, max)

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
                    html = createWrap(self.id, self.width, self.ratio,
                                      self.rows, self.cols, self.count,
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

    def createChart(self):

        layoutType = self.layout.get("type", "single")
        scaleType = self.layout.get("scales", "fixed")
        labelHeight = self.layout.get("labelHeight", 20)

        xScaleFree = (scaleType in ["free", "free_x"])  # if layoutType != "wrap" else True
        yScaleFree = (scaleType in ["free", "free_y"])

        html = self.createContainer(layoutType, xScaleFree, yScaleFree, labelHeight)
        html += dedent("""
        <script>
            window.hc_charts.promise.then(function(HC) {
        """)

        i = 0

        for row in range(self.rows):
            for col in range(self.cols):

                fig = Components().figure(zoomType="xy", exporting=False, title=None, legend=False)

                if i != self.count - 1:
                    fig.updateFigure(credits=False)

                if i < self.count:
                    for layer in self.layers:
                        mx, my = layer.mapping.get("x"), layer.mapping.get("y")

                        if layoutType == "single":
                            data = layer.data.getData()

                        elif layoutType == "wrap":
                            data = layer.data.getData(i)

                        elif layoutType == "grid":
                            data = layer.data.getData(col, row)

                        elif layoutType == "matrix":
                            mx = mx[col]
                            my = my[row]
                            data = layer.data.getData()

                        isEmpty = not (len(data) > 0)

                        opts = layer.getMinMax(xScaleFree, yScaleFree)
                        self._setMinMax(*opts)

                        data = layer.prepareData(data, mx, my)
                        fig.addSeries(my, data, layer.options)

                    fig.addXAxis(title=None, max=self.xmax, min=self.xmin,
                                 lineWidth=1, tickWidth=1, gridLineWidth=1)
                    fig.addYAxis(title=None, max=self.ymax, min=self.ymin,
                                 lineWidth=1, tickWidth=1, gridLineWidth=1)

                    if xScaleFree or row == self.rows - 1 or layoutType == "wrap":
                        fig.updateChart(marginBottom=40,
                                        height=(self.width // self.cols) * self.ratio + 30)
                    else:
                        fig.updateXAxis(labels=False)

                    if yScaleFree or col == 0:
                        fig.updateChart(marginLeft=50,   width=self.width // self.cols + 40)
                    else:
                        fig.updateYAxis(labels=False)

                container = "hc_%s_%d-%d" % (self.id, row, col)
                if isEmpty and xScaleFree and yScaleFree:
                    html += dedent("""
                    //      Chart %d-%d (empty)
                    """) % (row, col)
                else:
                    html += dedent("""
                    //      Chart %d-%d
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
