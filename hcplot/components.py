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

import hcplot.highcharts as hc


class Base(object):
    def _update(self, object, options):
        for k, v in options.items():
            setattr(object, k, v)


class Point(Base):
    def __init__(self, names, values, globalAlpha=None):
        self.point = hc.SeriesData()
        alpha = None
        color = None
        for name, value in zip(names, values):
            if name in ["x", "y"]:
                setattr(self.point, name, value)

            elif name == "alpha":
                alpha = value

            elif name == "shape":
                if self.point.marker is None:
                    self.point.marker = hc.Marker(symbol=value)
                self.point.marker.symbol = value

            elif name == "size":
                if self.point.marker is None:
                    self.point.marker = hc.Marker(radius=value)
                self.point.marker.radius = value

            elif name == "color":
                color = value

            if color is not None:
                if alpha is None and globalAlpha is None:
                    self.point.color = "rgb(%s)" % color
                else:
                    alpha = globalAlpha if alpha is None else alpha
                    self.point.color = "rgba(%s,%f)" % (color, alpha)

    def get(self):
        return self.point


class Axis(Base):
    def __init__(self, cls, labels=True, title=False, **options):
        if isinstance(labels, bool):
            options["labels"] = hc.AxisLabels(enabled=labels)
        else:
            options["labels"] = hc.AxisLabels(**labels)

        if isinstance(title, bool):
            options["title"] = hc.AxisTitle(enabled=False)
        else:
            options["title"] = hc.AxisTitle(**title)
        self.axis = cls(**options)

    def enableLabels(self, enabled):
        self.axis.labels.enabled = enabled

    def get(self):
        return self.axis


class XAxis(Axis):
    def __init__(self, labels=True, title=False, **options):
        super(__class__, self).__init__(hc.XAxis, labels, title, **options)  # noqa F821


class YAxis(Axis):
    def __init__(self, labels=True, title=False, **options):
        super(__class__, self).__init__(hc.YAxis, labels, title, **options)  # noqa F821


class Figure(Base):
    def __init__(self, chartOptions={}):
        if "title" in chartOptions.keys():
            self.title = hc.Title(text=chartOptions.pop("title"))
        else:
            self.title = hc.Title(text=None)

        if "exporting" in chartOptions.keys():
            self.exporting = hc.Exporting(enabled=chartOptions.pop("exporting"))
        else:
            self.exporting = hc.Exporting(enabled=True)

        if "legend" in chartOptions.keys():
            legend = chartOptions.pop("legend")
            if isinstance(legend, bool):
                self.legend = hc.Legend(enabled=legend)
            else:
                self.legend = hc.Legend(**legend)
        else:
            self.legend = hc.Legend(enabled=False)

        self.chart = hc.Chart(
            spacingBottom=5,
            spacingTop=5,
            spacingLeft=5,
            spacingRight=5,
            **chartOptions
        )
        self.credits = hc.Credits(enabled=True, position=hc.Position(y=-5))

        self.xAxis = None
        self.yAxis = None

        self.series = []

    def toDict(self):
        figure = hc.Figure(
            chart=self.chart,
            credits=self.credits,
            exporting=self.exporting,
            legend=self.legend,
            title=self.title
        )

        if self.xAxis is not None:
            figure.xAxis = self.xAxis.axis
        if self.yAxis is not None:
            figure.yAxis = self.yAxis.axis
        figure.series = self.series

        return figure.toDict()

    def enableCredits(self, enabled):
        self.credits.enabled = enabled
        return self

    def updateChart(self, **options):
        self._update(self.chart, options)
        return self

    def updateXAxis(self, **options):
        self._update(self.xAxis, options)
        return self

    def updateYAxis(self, **options):
        self._update(self.yAxis, options)
        return self

    def addXAxis(self, **options):
        self.xAxis = XAxis(**options)
        return self

    def addYAxis(self, **options):
        self.yAxis = YAxis(**options)
        return self

    def addSeries(self, series):
        self.series.append(series)
        return self
