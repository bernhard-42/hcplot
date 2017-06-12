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
from ..animation import _Animation
from ..datalabels import DataLabels
from ..events import Events, Point
from ..seriesdata import _SeriesData
from ..seriesstates import SeriesStates
from ..shadow import _Shadow
from ..tooltip import SeriesTooltip
from ..types import Function, Color, IntegerOrPercentageString, NumberOrString
from ..xyzaxis import XAxis, YAxis
from ..zone import Zone
from traitlets import Unicode, Bool, Integer, Instance, Float, List


class SeriesBase(HCBase):
    animationLimit = Integer(None, allow_none=True)
    className = Unicode(None, allow_none=True)
    color = Color(None, allow_none=True)
    cursor = Unicode(None, allow_none=True)
    data = List(_SeriesData, allow_none=True)
    description = Unicode(None, allow_none=True)
    events = Instance(Events, allow_none=True)
    exposeElementToA11y = Bool(None, allow_none=True)
    findNearestPointBy = Unicode(None, allow_none=True)
    getExtremesFromAll = Bool(None, allow_none=True)
    id_ = Unicode(None, allow_none=True)
    index = Integer(None, allow_none=True)
    keys = List(Unicode(allow_none=True))
    legendIndex = Integer(None, allow_none=True)
    name = Unicode(None, allow_none=True)
    point = Instance(Point, allow_none=True)
    pointDescriptionFormatter = Function(None, allow_none=True)
    selected = Bool(None, allow_none=True)
    skipKeyboardNavigation = Bool(None, allow_none=True)
    tooltip = Instance(SeriesTooltip, allow_none=True)
    visible = Bool(None, allow_none=True)
    zIndex = Integer(None, allow_none=True)


class SeriesBase2(SeriesBase):
    linkedTo = Unicode(None, allow_none=True)
    showInLegend = Bool(None, allow_none=True)
    stickyTracking = Bool(None, allow_none=True)


class SeriesBase3(SeriesBase2):
    allowPointSelect = Bool(None, allow_none=True)
    states = Instance(SeriesStates, allow_none=True)
    zoneAxis = Unicode(None, allow_none=True)
    zones = List(Instance(Zone))
    enableMouseTracking = Bool(None, allow_none=True)
    xAxis = Instance(XAxis, allow_none=True)
    yAxis = Instance(YAxis, allow_none=True)
    colorIndex = Integer(None, allow_none=True)
    showCheckbox = Bool(None, allow_none=True)


class SeriesBase4(SeriesBase3):
    pointIntervalUnit = Unicode(None, allow_none=True)
    pointStart = Float(None, allow_none=True)
    pointInterval = Float(None, allow_none=True)
    animation = _Animation(None, allow_none=True)
    dataLabels = Instance(DataLabels, allow_none=True)
    shadow = _Shadow(None, allow_none=True)


class SeriesBase5(SeriesBase2):
    allowPointSelect = Bool(None, allow_none=True)
    states = Instance(SeriesStates, allow_none=True)
    zoneAxis = Unicode(None, allow_none=True)
    zones = List(Instance(Zone))
    enableMouseTracking = Bool(None, allow_none=True)
    dataLabels = Instance(DataLabels, allow_none=True)
    shadow = _Shadow(None, allow_none=True)
    colors = List(Float(allow_none=False))
    borderColor = Color(None, allow_none=True)
    borderWidth = Integer(None, allow_none=True)
    depth = Integer(None, allow_none=True)
    minSize = Integer(None, allow_none=True)
    center = List(IntegerOrPercentageString(), maxLen=2)
    slicedOffset = Integer(None, allow_none=True)


class ColumnBase(SeriesBase4):
    pointPlacement = NumberOrString(None, allow_none=True)
    colors = List(Float(allow_none=False))
    borderColor = Color(None, allow_none=True)
    borderWidth = Integer(None, allow_none=True)
    depth = Integer(None, allow_none=True)
    softThreshold = Bool(None, allow_none=True)
    colorByPoint = Bool(None, allow_none=True)
    crisp = Bool(None, allow_none=True)
    maxPointWidth = Integer(None, allow_none=True)
    edgeColor = Color(None, allow_none=True)
    edgeWidth = Integer(None, allow_none=True)
    groupZPadding = Float(None, allow_none=True)
    pointPadding = Float(None, allow_none=True)
    pointRange = Float(None, allow_none=True)
    pointWidth = Integer(None, allow_none=True)
    borderRadius = Integer(None, allow_none=True)
    grouping = Bool(None, allow_none=True)
    groupPadding = Float(None, allow_none=True)


class MapBase(SeriesBase3):
    animation = _Animation(None, allow_none=True)
    dataLabels = Instance(DataLabels, allow_none=True)
    shadow = _Shadow(None, allow_none=True)
    colors = List(Float(allow_none=False))
    borderColor = Color(None, allow_none=True)
    borderWidth = Integer(None, allow_none=True)
    colorByPoint = Bool(None, allow_none=True)
    crisp = Bool(None, allow_none=True)
    turboThreshold = Integer(None, allow_none=True)
    cropThreshold = Integer(None, allow_none=True)
    maxPointWidth = Integer(None, allow_none=True)


class GaugeBase(SeriesBase2):
    xAxis = Instance(XAxis, allow_none=True)
    yAxis = Instance(YAxis, allow_none=True)
    animation = _Animation(None, allow_none=True)
    dataLabels = Instance(DataLabels, allow_none=True)
    shadow = _Shadow(None, allow_none=True)
    overshoot = Integer(None, allow_none=True)
    threshold = Integer(None, allow_none=True)
    wrap = Bool(None, allow_none=True)
