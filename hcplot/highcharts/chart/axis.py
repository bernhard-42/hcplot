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
from .attributes import Label, PlotLine, PlotBands, Break, StackLabels


class Axis(HCBase):

    def __init__(self, allowDecimals=None, alternateGridColor=None, breaks=None, categories=None,
                 ceiling=None, className=None, crosshair=None, dateTimeLabelFormats=None,
                 description=None, endOnTick=None, events=None, floor=None, gridLineColor=None,
                 gridLineDashStyle=None, gridLineWidth=None, id_=None, labels=None, lineColor=None,
                 lineWidth=None, linkedTo=None, max_=None, maxPadding=None, maxZoom=None, min_=None,
                 minPadding=None, minRange=None, minTickInterval=None, minorGridLineColor=None,
                 minorGridLineDashStyle=None, minorGridLineWidth=None, minorTickColor=None,
                 minorTickInterval=None, minorTickLength=None, minorTickPosition=None,
                 minorTickWidth=None, offset=None, opposite=None, plotBands=None, plotLines=None,
                 reversed_=None, showEmpty=None, showFirstLabel=None, showLastLabel=None,
                 softMax=None, softMin=None, startOfWeek=None, startOnTick=None, tickAmount=None,
                 tickColor=None, tickInterval=None, tickLength=None, tickPixelInterval=None,
                 tickPosition=None, tickPositioner=None, tickPositions=None, tickWidth=None,
                 tickmarkPlacement=None, title=None, type_=None, uniqueNames=None, units=None,
                 visible=None):

        self.check("label", labels, Label)
        self.check("plotLines", plotLines, PlotLine, True)
        self.check("plotBands", plotBands, PlotBands, True)
        self.check("title", title, title)
        self.check("crosshair", crosshair, crosshair)
        super(__class__, self).__init__(locals())         # noqa F821


class XAxis(Axis):

    def __init__(self, breaks=None, **kwargs):

        self.check("breaks", breaks, Break, True)

        super(__class__, self).__init__(**kwargs)       # noqa F821
        params = {"breaks": breaks}
        self.setIfExists(params)


class YAxis(Axis):

    def __init__(self, angle=None, breaks=None, gridLineInterpolation=None, gridZIndex=None,
                 maxColor=None, minColor=None, reversedStacks=None, stackLabels=None, stops=None):

        self.check("stackLabels", stackLabels, StackLabels)
        self.check("breaks", breaks, Break, True)

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"angle": angle, "breaks": breaks, "gridLineInterpolation": gridLineInterpolation,
                  "gridZIndex": gridZIndex, "maxColor": maxColor, "minColor": minColor,
                  "reversedStacks": reversedStacks, "stackLabels": stackLabels, "stops": stops}
        self.setIfExists(params)


class ZAxis(Axis):

    def __init__(self, **kwargs):

        super(__class__, self).__init__(**kwargs)         # noqa F821
