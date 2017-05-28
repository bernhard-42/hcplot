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

from .base import SeriesBase4


class AreaSplineRange(SeriesBase4):

    def __init__(self, pointPlacement=None, lineWidth=None, dashStyle=None, turboThreshold=None,
                 cropThreshold=None, negativeColor=None, linecap=None, connectNulls=None, fillColor=None,
                 lineColor=None, fillOpacity=None, negativeFillColor=None, trackByArea=None,
                 **kwargs):

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"pointPlacement": pointPlacement, "lineWidth": lineWidth, "dashStyle": dashStyle,
                  "turboThreshold": turboThreshold, "cropThreshold": cropThreshold,
                  "negativeColor": negativeColor, "linecap": linecap, "connectNulls": connectNulls,
                  "fillColor": fillColor, "lineColor": lineColor, "fillOpacity": fillOpacity,
                  "negativeFillColor": negativeFillColor, "trackByArea": trackByArea}
        self.setIfExists(params)
