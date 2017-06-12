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

from traitlets import Undefined, TraitType

from .charts.area import Area, AreaOptions                                                 # noqa F401
from .charts.arearange import AreaRange, AreaRangeOptions                                  # noqa F401
from .charts.areaspline import AreaSpline, AreaSplineOptions                               # noqa F401
from .charts.areasplinerange import AreaSplineRange, AreaSplineRangeOptions                # noqa F401
from .charts.bar import Bar, BarOptions                                                    # noqa F401
from .charts.boxplot import BoxPlot, BoxPlotOptions                                        # noqa F401
from .charts.bubble import Bubble, BubbleOptions                                           # noqa F401
from .charts.column import Column, ColumnOptions                                           # noqa F401
from .charts.columnrange import ColumnRange, ColumnRangeOptions                            # noqa F401
from .charts.errorbar import ErrorBar, ErrorBarOptions                                     # noqa F401
from .charts.funnel import Funnel, FunnelOptions                                           # noqa F401
from .charts.gauge import Gauge, GaugeOptions                                              # noqa F401
from .charts.heatmap import HeatMap, HeatMapOptions                                        # noqa F401
from .charts.line import Line, LineOptions                                                 # noqa F401
from .charts.pie import Pie, PieOptions                                                    # noqa F401
from .charts.polygon import Polygon, PolygonOptions                                        # noqa F401
from .charts.pyramid import Pyramid, PyramidOptions                                        # noqa F401
from .charts.scatter import Scatter, ScatterOptions                                        # noqa F401
from .charts.solidgauge import SolidGauge, SolidGaugeOptions                               # noqa F401
from .charts.spline import Spline, SplineOptions                                           # noqa F401
from .charts.treemap import TreeMap, TreeMapOptions                                        # noqa F401
from .charts.waterfall import Waterfall, WaterfallOptions                                  # noqa F401

AllSeries = [Area, AreaRange, AreaSpline, AreaSplineRange, Bar, BoxPlot, Bubble, Column,
             ColumnRange, ErrorBar, Funnel, Gauge, HeatMap, Line, Pie, Polygon, Pyramid,
             Scatter, SolidGauge, Spline, TreeMap, Waterfall]

AllSeriesOptions = [AreaOptions, AreaRangeOptions, AreaSplineOptions, AreaSplineRangeOptions, BarOptions,
                    BoxPlotOptions, BubbleOptions, ColumnOptions, ColumnRangeOptions, ErrorBarOptions,
                    FunnelOptions, GaugeOptions, HeatMapOptions, LineOptions, PieOptions, PolygonOptions,
                    PyramidOptions, ScatterOptions, SolidGaugeOptions, SplineOptions, TreeMapOptions,
                    WaterfallOptions]


class Series(TraitType):
    default_value = None
    info_text = 'Any Chart Object or ChartOptions object'

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        super(__class__, self).__init__(default_value=default_value,          # noqa F821
                                        allow_none=allow_none, **kwargs)

    def validate(self, obj, value):
        if value is None or type(value) in AllSeries + AllSeriesOptions:
            return value
        else:
            self.error(obj, value)


class SeriesOptions(TraitType):
    default_value = None
    info_text = 'Any ChartOptions Object'

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        super(__class__, self).__init__(default_value=default_value,          # noqa F821
                                        allow_none=allow_none, **kwargs)

    def validate(self, obj, value):
        if value is None or type(value) in AllSeriesOptions:
            return value
        else:
            self.error(obj, value)
