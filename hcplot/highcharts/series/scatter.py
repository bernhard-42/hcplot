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
from .marker import Marker


class Scatter(SeriesBase4):
    def __init__(self, softThreshold=None, lineWidth=None, dashStyle=None, threshold=None,
                 turboThreshold=None, cropThreshold=None, negativeColor=None, marker=None,
                 **kwargs):

        self.check("marker", marker, Marker)

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"softThreshold": softThreshold, "lineWidth": lineWidth, "dashStyle": dashStyle,
                  "threshold": threshold, "turboThreshold": turboThreshold, "cropThreshold": cropThreshold,
                  "negativeColor": negativeColor, "marker": marker}
        self.setIfExists(params)
