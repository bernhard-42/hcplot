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

from ..layer import Layer
from ..utils.color import web2rgba, rgba2web
from ..components import Point
from ..highcharts import Marker
from ..highcharts.charts import Scatter


class Points(Layer):

    def __init__(self, *dataOrConfigs,
                 position=None, showLegend=False, color="#7cb5ec", alpha=None,
                 lineWidth=0, lineColor=None, size=None, shape=None):

        super(__class__, self).__init__(dataOrConfigs, position, showLegend,        # noqa F821
                                        color=color, alpha=alpha,
                                        lineWidth=0, lineColor=None, size=size, shape=shape)

        marker = Marker(
            radius=(3 if size is None else size),
            symbol=("diamond" if shape is None else shape)
        )

        rgba = web2rgba(color)
        if alpha is not None:
            rgba = rgba[:3] + (alpha,)

        self.series = Scatter(marker=marker, color=rgba2web(rgba))

        if lineWidth > 0:
            self.series.marker.lineWidth = lineWidth

        if lineColor is not None:
            self.series.marker.lineColor = rgba2web(lineColor)

    def getSeries(self, df, mx, my):
        mapping = {"x": mx, "y": my}
        if df.shape[0] > self.figure.performanceTreshold:
            cols = list(mapping.values())
            df2 = df[cols]
            self.series.data = df2.to_dict("split")["data"]
        else:
            mapping.update(self.usePlotLevel)
            names = list(mapping.keys())
            cols = list(mapping.values())
            df2 = df[cols].copy()
            df2.columns = names

            data = df2.to_dict("split")["data"]

            self.series.data = [Point(names, values, self.alpha).get() for values in data]
        self.series.name = my

        return self.series
