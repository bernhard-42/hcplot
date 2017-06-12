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
from .series import AreaOptions, AreaRangeOptions, AreaSplineOptions, AreaSplineRangeOptions, BarOptions, \
    BoxPlotOptions, BubbleOptions, ColumnOptions, ColumnRangeOptions, ErrorBarOptions, FunnelOptions, \
    GaugeOptions, HeatMapOptions, LineOptions, PieOptions, PolygonOptions, PyramidOptions, ScatterOptions, \
    SolidGaugeOptions, SplineOptions, TreeMapOptions, WaterfallOptions
from .series import SeriesOptions
from traitlets import Instance


class PlotOptions(HCBase):
    area = Instance(AreaOptions, allow_none=True)
    arearange = Instance(AreaRangeOptions, allow_none=True)
    areaspline = Instance(AreaSplineOptions, allow_none=True)
    areasplinerange = Instance(AreaSplineRangeOptions, allow_none=True)
    bar = Instance(BarOptions, allow_none=True)
    boxplot = Instance(BoxPlotOptions, allow_none=True)
    bubble = Instance(BubbleOptions, allow_none=True)
    column = Instance(ColumnOptions, allow_none=True)
    columnrange = Instance(ColumnRangeOptions, allow_none=True)
    errorbar = Instance(ErrorBarOptions, allow_none=True)
    funnel = Instance(FunnelOptions, allow_none=True)
    gauge = Instance(GaugeOptions, allow_none=True)
    heatmap = Instance(HeatMapOptions, allow_none=True)
    line = Instance(LineOptions, allow_none=True)
    pie = Instance(PieOptions, allow_none=True)
    polygon = Instance(PolygonOptions, allow_none=True)
    pyramid = Instance(PyramidOptions, allow_none=True)
    scatter = Instance(ScatterOptions, allow_none=True)
    series = SeriesOptions(None, allow_none=True)
    solidgauge = Instance(SolidGaugeOptions, allow_none=True)
    spline = Instance(SplineOptions, allow_none=True)
    treemap = Instance(TreeMapOptions, allow_none=True)
    waterfall = Instance(WaterfallOptions, allow_none=True)
