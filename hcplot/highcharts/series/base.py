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
from .attributes import Data, Events, Point, Tooltip, States, Zones, Datalabels


class SeriesBase(HCBase):

    def __init__(self, animationLimit=None, className=None, color=None, cursor=None, data=None,
                 description=None, events=None, exposeElementToA11y=None, findNearestPointBy=None,
                 getExtremesFromAll=None, id_=None, index=None, keys=None, legendIndex=None, name=None,
                 point=None, pointDescriptionFormatter=None, selected=None, skipKeyboardNavigation=None,
                 tooltip=None, visible=None, zIndex=None):

        self.check("data", data, Data)
        self.check("events", events, Events)
        self.check("point", point, Point)
        self.check("tooltip", tooltip, Tooltip)

        super(__class__, self).__init__(locals())         # noqa F821


class SeriesBase2(SeriesBase):

    def __init__(self, linkedTo=None, showInLegend=None, stickyTracking=None,
                 **kwargs):

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"linkedTo": linkedTo, "showInLegend": showInLegend, "stickyTracking": stickyTracking}
        self.setIfExists(params)


class SeriesBase3(SeriesBase2):

    def __init__(self, allowPointSelect=None, states=None, zoneAxis=None, zones=None,
                 enableMouseTracking=None, xAxis=None, yAxis=None, colorIndex=None, showCheckbox=None,
                 **kwargs):
        self.check("states", states, States)
        self.check("zones", zones, Zones)

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"allowPointSelect": allowPointSelect, "states": states, "zoneAxis": zoneAxis,
                  "zones": zones, "enableMouseTracking": enableMouseTracking, "xAxis": xAxis,
                  "yAxis": yAxis, "colorIndex": colorIndex, "showCheckbox": showCheckbox, }
        self.setIfExists(params)


class SeriesBase4(SeriesBase3):

    def __init__(self, pointIntervalUnit=None, pointStart=None, pointInterval=None, animation=None,
                 dataLabels=None, shadow=None,
                 **kwargs):

        self.check("dataLabels", dataLabels, Datalabels)

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"pointIntervalUnit": pointIntervalUnit, "pointStart": pointStart,
                  "pointInterval": pointInterval, "animation": animation, "dataLabels": dataLabels,
                  "shadow": shadow}
        self.setIfExists(params)


class SeriesBase5(SeriesBase2):

    def __init__(self, allowPointSelect=None, states=None, zoneAxis=None, zones=None,
                 enableMouseTracking=None, dataLabels=None, shadow=None, colors=None,
                 borderColor=None, borderWidth=None, depth=None, MinSize=None,
                 center=None, slicedOffset=None,
                 **kwargs):

        self.check("states", states, States)
        self.check("zones", zones, Zones)
        self.check("dataLabels", dataLabels, Datalabels)

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"allowPointSelect": allowPointSelect, "states": states, "zoneAxis": zoneAxis,
                  "zones": zones, "enableMouseTracking": enableMouseTracking, "dataLabels": dataLabels,
                  "shadow": shadow, "colors": colors, "borderColor": borderColor, "borderWidth": borderWidth,
                  "depth": depth, "MinSize": MinSize, "center": center, "slicedOffset": slicedOffset, }
        self.setIfExists(params)


class ColumnBase(SeriesBase4):

    def __init__(self, pointPlacement=None, colors=None, borderColor=None, borderWidth=None, depth=None,
                 softThreshold=None, colorByPoint=None, crisp=None, maxPointWidth=None, edgeColor=None,
                 edgeWidth=None, groupZPadding=None, pointPadding=None, pointRange=None, pointWidth=None,
                 borderRadius=None, grouping=None, groupPadding=None,
                 **kwargs):

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"pointPlacement": pointPlacement, "colors": colors, "borderColor": borderColor,
                  "borderWidth": borderWidth, "depth": depth, "softThreshold": softThreshold,
                  "colorByPoint": colorByPoint, "crisp": crisp, "maxPointWidth": maxPointWidth,
                  "edgeColor": edgeColor, "edgeWidth": edgeWidth, "groupZPadding": groupZPadding,
                  "pointPadding": pointPadding, "pointRange": pointRange, "pointWidth": pointWidth,
                  "borderRadius": borderRadius, "grouping": grouping, "groupPadding": groupPadding}

        self.setIfExists(params)


class MapBase(SeriesBase3):

    def __init__(self, animation=None, dataLabels=None, shadow=None, colors=None, borderColor=None,
                 borderWidth=None, colorByPoint=None, crisp=None, turboThreshold=None, cropThreshold=None,
                 maxPointWidth=None,
                 **kwargs):

        self.check("dataLabels", dataLabels, Datalabels)

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"animation": animation, "dataLabels": dataLabels, "shadow": shadow, "colors": colors,
                  "borderColor": borderColor, "borderWidth": borderWidth, "colorByPoint": colorByPoint,
                  "crisp": crisp, "turboThreshold": turboThreshold, "cropThreshold": cropThreshold,
                  "maxPointWidth": maxPointWidth}
        self.setIfExists(params)


class GaugeBase(SeriesBase2):

    def __init__(self, xAxis=None, yAxis=None, animation=None, dataLabels=None, shadow=None, overshoot=None,
                 threshold=None, wrap=None,
                 **kwargs):

        self.check("dataLabels", dataLabels, Datalabels)

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"xAxis": xAxis, "yAxis": yAxis, "animation": animation, "dataLabels": dataLabels,
                  "shadow": shadow, "overshoot": overshoot, "threshold": threshold, "wrap": wrap}
        self.setIfExists(params)
