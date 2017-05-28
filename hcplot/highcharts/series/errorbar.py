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

from .base import SeriesBase3


class ErrorBar(SeriesBase3):
    def __init__(self, pointIntervalUnit=None, pointStart=None, pointInterval=None, pointPlacement=None,
                 colors=None, depth=None, colorByPoint=None, crisp=None, lineWidth=None, turboThreshold=None,
                 negativeColor=None, maxPointWidth=None, edgeColor=None, edgeWidth=None, groupZPadding=None,
                 pointPadding=None, pointRange=None, pointWidth=None, stemColor=None, StemDashStyle=None,
                 stemWidth=None, whiskerColor=None, whiskerLength=None, whiskerWidth=None,
                 **kwargs):

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"pointIntervalUnit": pointIntervalUnit, "pointStart": pointStart,
                  "pointInterval": pointInterval, "pointPlacement": pointPlacement, "colors": colors,
                  "depth": depth, "colorByPoint": colorByPoint, "crisp": crisp, "lineWidth": lineWidth,
                  "turboThreshold": turboThreshold, "negativeColor": negativeColor,
                  "maxPointWidth": maxPointWidth, "edgeColor": edgeColor, "edgeWidth": edgeWidth,
                  "groupZPadding": groupZPadding, "pointPadding": pointPadding, "pointRange": pointRange,
                  "pointWidth": pointWidth, "stemColor": stemColor, "StemDashStyle": StemDashStyle,
                  "stemWidth": stemWidth, "whiskerColor": whiskerColor, "whiskerLength": whiskerLength,
                  "whiskerWidth": whiskerWidth}
        self.setIfExists(params)
