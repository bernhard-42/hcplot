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

from .base import HCBase
from .color import Color
from .crosshair import _CrossHair
from .types import Function, CSSObject, FloatOrAuto, Float64
from .position import XYFloat
from .events import PlotEvents
from traitlets import Unicode, Bool, Integer, Instance, Float, List, Tuple, Any, Dict


class Break(HCBase):
    breakSize = Integer(None, allow_none=True)
    from_ = Integer(None, allow_none=True)
    repeat = Integer(None, allow_none=True)
    to = Integer(None, allow_none=True)


class AxisEvents(HCBase):
    afterBreaks = Function(None, allow_none=True)
    afterSetExtremes = Function(None, allow_none=True)
    pointBreak = Function(None, allow_none=True)
    pointInBreak = Function(None, allow_none=True)
    setExtremes = Function(None, allow_none=True)


class AxisLabels(XYFloat):
    align = Unicode(None, allow_none=True)
    autoRotation = List(Float(allow_none=True))
    autoRotationLimit = Float(None, allow_none=True)
    distance = Integer(None, allow_none=True)
    enabled = Bool(None, allow_none=True)
    format_ = Unicode(None, allow_none=True)
    formatter = Function(None, allow_none=True)
    maxStaggerLines = Integer(None, allow_none=True)
    overflow = Unicode(None, allow_none=True)
    padding = Integer(None, allow_none=True)
    reserveSpace = Bool(None, allow_none=True)
    rotation = Float(None, allow_none=True)
    staggerLines = Integer(None, allow_none=True)
    step = Float(None, allow_none=True)
    style = CSSObject(None, allow_none=True)
    useHTML = Bool(None, allow_none=True)
    zIndex = Integer(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class PlotLabel(XYFloat):
    align = Unicode(None, allow_none=True)
    rotation = Float(None, allow_none=True)
    style = CSSObject(None, allow_none=True)
    text = Unicode(None, allow_none=True)
    textAlign = Unicode(None, allow_none=True)
    useHTML = Bool(None, allow_none=True)
    verticalAlign = Unicode(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class PlotBand(HCBase):
    borderColor = Color(None, allow_none=True)
    borderWidth = Integer(None, allow_none=True)
    className = Unicode(None, allow_none=True)
    color = Color(None, allow_none=True)
    events = Instance(PlotEvents, allow_none=True)
    from_ = Float(None, allow_none=True)
    id_ = Unicode(None, allow_none=True)
    label = Instance(PlotLabel, allow_none=True)
    to = Float(None, allow_none=True)
    zIndex = Integer(None, allow_none=True)


class PlotLine(HCBase):
    className = Unicode(None, allow_none=True)
    color = Color(None, allow_none=True)
    dashStyle = Unicode(None, allow_none=True)
    events = Instance(PlotEvents, allow_none=True)
    id_ = Unicode(None, allow_none=True)
    label = Instance(PlotLabel, allow_none=True)
    value = Float(None, allow_none=True)
    width = Integer(None, allow_none=True)
    zIndex = Integer(None, allow_none=True)


class AxisTitle(XYFloat):
    align = Unicode(None, allow_none=True)
    enabled = Bool(None, allow_none=True)
    margin = Integer(None, allow_none=True)
    offset = Integer(None, allow_none=True)
    reserveSpace = Bool(None, allow_none=True)
    rotation = Float(None, allow_none=True)
    style = CSSObject(None, allow_none=True)
    text = Unicode(None, allow_none=True)
    x = Float(None, allow_none=True)
    y = Float(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class StackLabels(XYFloat):
    align = Unicode(None, allow_none=True)
    enabled = Bool(None, allow_none=True)
    format_ = Unicode(None, allow_none=True)
    formatter = Function(None, allow_none=True)
    rotation = Float(None, allow_none=True)
    style = CSSObject(None, allow_none=True)
    textAlign = Unicode(None, allow_none=True)
    useHTML = Bool(None, allow_none=True)
    verticalAlign = Unicode(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class ZAxis(HCBase):
    allowDecimals = Bool(None, allow_none=True)
    alternateGridColor = Color(None, allow_none=True)
    categories = List(Unicode())
    ceiling = Float(None, allow_none=True)
    className = Unicode(None, allow_none=True)
    crosshair = _CrossHair(None, allow_none=True)
    dateTimeLabelFormats = Dict(None, allow_none=True)    # TODO millisecond,second,minute,hour,day,month,year
    description = Unicode(None, allow_none=True)
    endOnTick = Bool(None, allow_none=True)
    events = Instance(AxisEvents, allow_none=True)
    floor = Float(None, allow_none=True)
    gridLineColor = Color(None, allow_none=True)
    gridLineDashStyle = Unicode(None, allow_none=True)
    gridLineWidth = Integer(None, allow_none=True)
    gridZIndex = Integer(None, allow_none=True)
    id_ = Unicode(None, allow_none=True)
    labels = Instance(AxisLabels, allow_none=True)
    lineColor = Color(None, allow_none=True)
    lineWidth = Integer(None, allow_none=True)
    linkedTo = Integer(None, allow_none=True)
    max_ = Float64(None, allow_none=True)
    maxPadding = Integer(None, allow_none=True)
    maxZoom = Integer(None, allow_none=True)
    min_ = Float64(None, allow_none=True)
    minPadding = Integer(None, allow_none=True)
    minRange = Integer(None, allow_none=True)
    minTickInterval = Float(None, allow_none=True)
    minorGridLineColor = Color(None, allow_none=True)
    minorGridLineDashStyle = Unicode(None, allow_none=True)
    minorGridLineWidth = Integer(None, allow_none=True)
    minorTickColor = Color(None, allow_none=True)
    minorTickInterval = FloatOrAuto(None, allow_none=True)
    minorTickLength = Integer(None, allow_none=True)
    minorTickPosition = Unicode(None, allow_none=True)
    minorTickWidth = Integer(None, allow_none=True)
    offset = Integer(None, allow_none=True)
    opposite = Bool(None, allow_none=True)
    plotBands = List(Instance(PlotBand, allow_none=False), allow_none=True)
    plotLines = List(Instance(PlotLine, allow_none=False), allow_none=True)
    reversed_ = Bool(None, allow_none=True)
    showEmpty = Bool(None, allow_none=True)
    showFirstLabel = Bool(None, allow_none=True)
    showLastLabel = Bool(None, allow_none=True)
    softMax = Float(None, allow_none=True)
    softMin = Float(None, allow_none=True)
    startOfWeek = Integer(None, allow_none=True)
    startOnTick = Bool(None, allow_none=True)
    tickAmount = Integer(None, allow_none=True)
    tickColor = Color(None, allow_none=True)
    tickInterval = Float(None, allow_none=True)
    tickLength = Float(None, allow_none=True)
    tickPixelInterval = Integer(None, allow_none=True)
    tickPosition = Unicode(None, allow_none=True)
    tickPositioner = Function(None, allow_none=True)
    tickPositions = List(Float(allow_none=False))
    tickWidth = Integer(None, allow_none=True)
    tickmarkPlacement = Unicode(None, allow_none=True)
    title = Instance(AxisTitle, allow_none=True)
    type_ = Unicode(None, allow_none=True)
    uniqueNames = Bool(None, allow_none=True)
    units = List(List(Any()))
    visible = Bool(None, allow_none=True)


class XAxis(ZAxis):
    breaks = List(Instance(Break, allow_none=False), allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class YAxis(XAxis):
    gridLineInterpolation = Unicode(None, allow_none=True)
    gridZIndex = Integer(None, allow_none=True)
    maxColor = Color(None, allow_none=True)
    minColor = Color(None, allow_none=True)
    reversedStacks = Bool(None, allow_none=True)
    stackLabels = Instance(StackLabels, allow_none=True)
    stops = List(Tuple(Float(), Color()))

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821
