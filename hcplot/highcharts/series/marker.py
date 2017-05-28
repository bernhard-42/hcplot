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

from ..base import HCBase


class MarkerHover(HCBase):

    def __init__(self, enabled=None, fillColor=None, lineColor=None, lineWidth=None, lineWidthPlus=None,
                 radius=None, radiusPlus=None,
                 **kwargs):

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"enabled": enabled, "fillColor": fillColor, "lineColor": lineColor, "lineWidth": lineWidth,
                  "lineWidthPlus": lineWidthPlus, "radius": radius, "radiusPlus": radiusPlus}
        self.setIfExists(params)


class MarkerSelect(HCBase):

    def __init__(self, enabled=None, fillColor=None, lineColor=None, lineWidth=None, radius=None,
                 **kwargs):

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"enabled": enabled, "fillColor": fillColor, "lineColor": lineColor, "lineWidth": lineWidth,
                  "radius": radius}
        self.setIfExists(params)


class MarkerStates(HCBase):

    def __init__(self, hover=None, select=None,
                 **kwargs):

        self.check("hover", hover, MarkerHover)
        self.check("select", select, MarkerSelect)

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"hover": hover, "select": select}
        self.setIfExists(params)


class Marker(HCBase):

    def __init__(self, enabled=None, fillColor=None, height=None, lineColor=None, lineWidth=None,
                 radius=None, states=None, symbol=None, width=None, **kwargs):

        self.check("states", states, MarkerStates)

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"enabled": enabled, "fillColor": fillColor, "height": height, "lineColor": lineColor,
                  "lineWidth": lineWidth, "radius": radius, "states": states, "symbol": symbol,
                  "width": width}
        self.setIfExists(params)
