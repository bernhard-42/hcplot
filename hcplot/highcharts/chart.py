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
from .buttons import ResetZoomButton
from .color import Color
from .credits import Credits
from .data import Data
from .drilldown import DrillDown
from .events import ChartEvents
from .labels import Labels
from .legend import Legend
from .navigation import Navigation
from .nodata import NoData
from .options3d import Options3d
from .pane import Pane
from .plotoptions import PlotOptions
from .series import Series
from .title import SubTitle, Title
from .tooltip import Tooltip
from .types import CSSObject, NumberOrString
from .animation import _Animation
from .shadow import _Shadow
from .xyzaxis import XAxis, YAxis, ZAxis
from traitlets import Instance, List, Bool, Unicode, Integer


class Chart(HCBase):
    alignTicks = Bool(None, allow_none=True)
    animation = _Animation(None, allow_none=True)
    backgroundColor = Color(None, allow_none=True)
    borderColor = Color(None, allow_none=True)
    borderRadius = Integer(None, allow_none=True)
    borderWidth = Integer(None, allow_none=True)
    className = Unicode(None, allow_none=True)
    colorCount = Integer(None, allow_none=True)
    defaultSeriesType = Unicode(None, allow_none=True)
    description = Unicode(None, allow_none=True)
    events = Instance(ChartEvents, allow_none=True)
    height = NumberOrString(None, allow_none=True)
    ignoreHiddenSeries = Bool(None, allow_none=True)
    inverted = Bool(None, allow_none=True)
    margin = List(Integer(allow_none=False), minLen=4, maxLen=4)
    marginBottom = Integer(None, allow_none=True)
    marginLeft = Integer(None, allow_none=True)
    marginRight = Integer(None, allow_none=True)
    margIntop = Integer(None, allow_none=True)
    options3d = Instance(Options3d, allow_none=True)
    panKey = Unicode(None, allow_none=True)
    panning = Bool(None, allow_none=True)
    pinchType = Unicode(None, allow_none=True)
    plotBackgroundColor = Color(None, allow_none=True)
    plotBackgroundImage = Unicode(None, allow_none=True)
    plotBorderColor = Color(None, allow_none=True)
    plotBorderWidth = Integer(None, allow_none=True)
    plotShadow = _Shadow(None, allow_none=True)
    polar = Bool(None, allow_none=True)
    reflow = Bool(None, allow_none=True)
    renderTo = Unicode(None, allow_none=True)
    resetZoomButton = Instance(ResetZoomButton, allow_none=True)
    selectionMarkerFill = Color(None, allow_none=True)
    shadow = _Shadow(None, allow_none=True)
    showAxes = Bool(None, allow_none=True)
    spacing = List(Integer(allow_none=False), minLen=4, maxLen=4)
    spacingBottom = Integer(None, allow_none=True)
    spacingLeft = Integer(None, allow_none=True)
    spacingRight = Integer(None, allow_none=True)
    spacingTop = Integer(None, allow_none=True)
    style = CSSObject(None, allow_none=True)
    type_ = Unicode(None, allow_none=True)
    typeDescription = Unicode(None, allow_none=True)
    width = Integer(None, allow_none=True)
    zoomType = Unicode(None, allow_none=True)


class ChartOptions(HCBase):
    chart = Instance(Chart, allow_none=True)
    colors = List(Color, allow_none=True)
    credits = Instance(Credits, allow_none=True)
    data = Instance(Data, allow_none=True)
    drilldown = Instance(DrillDown, allow_none=True)
    labels = Instance(Labels, allow_none=True)
    legend = Instance(Legend, allow_none=True)
    navigation = Instance(Navigation, allow_none=True)
    noData = Instance(NoData, allow_none=True)
    pane = Instance(Pane, allow_none=True)
    plotOptions = Instance(PlotOptions, allow_none=True)
    series = List(Series(None, allow_none=True))
    subtitle = Instance(SubTitle, allow_none=True)
    title = Instance(Title, allow_none=True)
    tooltip = Instance(Tooltip, allow_none=True)
    xAxis = Instance(XAxis, allow_none=True)
    yAxis = Instance(YAxis, allow_none=True)
    zAxis = Instance(ZAxis, allow_none=True)
