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
from ..figure.attributes import Style


class PointEvents(HCBase):

    def __init__(self, **kwargs):

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {}
        self.setIfExists(params)


class Data(HCBase):
    def __init__(self, className=None, color=None, colorIndex=None, dataLabels=None, description=None,
                 drilldown=None, events=None, id_=None, isIntermediateSum=None, isSum=None, labelrank=None,
                 name=None, selected=None, x=None, y=None,
                 **kwargs):

        self.check("events", events, PointEvents)

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"className": className, "color": color, "colorIndex": colorIndex, "dataLabels": dataLabels,
                  "description": description, "drilldown": drilldown, "events": events, "id_": id_,
                  "isIntermediateSum": isIntermediateSum, "isSum": isSum, "labelrank": labelrank,
                  "name": name, "selected": selected, "x": x, "y": y}
        self.setIfExists(params)


class Datalabels(HCBase):
    def __init__(self, align=None, allowOverlap=None, backgroundColor=None, borderColor=None,
                 borderRadius=None, borderWidth=None, className=None, color=None, crop=None, defer=None,
                 enabled=None, format=None, formatter=None, inside=None, overflow=None, padding=None,
                 rotation=None, shadow=None, shape=None, style=None, useHTML=None, verticalAlign=None,
                 x=None, y=None, zIndex=None, **kwargs):

        self.check("style", style, Style)

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"align": align, "allowOverlap": allowOverlap, "backgroundColor": backgroundColor,
                  "borderColor": borderColor, "borderRadius": borderRadius, "borderWidth": borderWidth,
                  "className": className, "color": color, "crop": crop, "defer": defer, "enabled": enabled,
                  "format": format, "formatter": formatter, "inside": inside, "overflow": overflow,
                  "padding": padding, "rotation": rotation, "shadow": shadow, "shape": shape,
                  "style": style, "useHTML": useHTML, "verticalAlign": verticalAlign, "x": x, "y": y,
                  "zIndex": zIndex}
        self.setIfExists(params)


class Events(HCBase):

    def __init__(self, afterAnimate=None, checkboxClick=None, click=None, hide=None, legendItemClick=None,
                 mouseOut=None, mouseOver=None, show=None,
                 **kwargs):

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"afterAnimate": afterAnimate, "checkboxClick": checkboxClick, "click": click, "hide": hide,
                  "legendItemClick": legendItemClick, "mouseOut": mouseOut, "mouseOver": mouseOver,
                  "show": show}
        self.setIfExists(params)


class Point(HCBase):

    def __init__(self, events=None, **kwargs):

        self.check("events", events, PointEvents)

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"events": events}
        self.setIfExists(params)


class Tooltip(HCBase):
    def __init__(self, dateTimeLabelFormats=None, followPointer=None, followTouchMove=None,
                 footerFormat=None, headerFormat=None, hideDelay=None, padding=None, pointFormat=None,
                 pointFormatter=None, split=None, valueDecimals=None, valuePrefix=None, valueSuffix=None,
                 xDateFormat=None,
                 **kwargs):

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"dateTimeLabelFormats": dateTimeLabelFormats, "followPointer": followPointer,
                  "followTouchMove": followTouchMove, "footerFormat": footerFormat,
                  "headerFormat": headerFormat, "hideDelay": hideDelay, "padding": padding,
                  "pointFormat": pointFormat, "pointFormatter": pointFormatter, "split": split,
                  "valueDecimals": valueDecimals, "valuePrefix": valuePrefix, "valueSuffix": valueSuffix,
                  "xDateFormat": xDateFormat}
        self.setIfExists(params)


class Animation(HCBase):

    def __init__(self, duration=None,
                 **kwargs):

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"duration": duration}
        self.setIfExists(params)


class Halo(HCBase):

    def __init__(self, attributes=None, opacity=None, size=None, **kwargs):

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"attributes": attributes, "opacity": opacity, "size": size}
        self.setIfExists(params)


class Hover(HCBase):

    def __init__(self, animation=None, borderColor=None, brightness=None, color=None, enabled=None, halo=None,
                 **kwargs):

        self.check("animation", animation, Animation)
        self.check("halo", halo, Halo)

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"animation": animation, "borderColor": borderColor, "brightness": brightness,
                  "color": color, "enabled": enabled, "halo": halo}
        self.setIfExists(params)


class States(HCBase):

    def __init__(self, hover=None, **kwargs):

        self.check("hover", hover, Hover)

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"hover": hover}
        self.setIfExists(params)


class Zones(HCBase):

    def __init__(self, className=None, color=None, dashStyle=None, fillColor=None, value=None,
                 **kwargs):

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"className": className, "color": color, "dashStyle": dashStyle, "fillColor": fillColor,
                  "value": value}
        self.setIfExists(params)
