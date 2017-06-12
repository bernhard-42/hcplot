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
from traitlets import Instance
from .types import Function


class ChartEvents(HCBase):
    addSeries = Function(None, allow_none=True)
    afterPrInt = Function(None, allow_none=True)
    beforePrInt = Function(None, allow_none=True)
    click = Function(None, allow_none=True)
    drilldown = Function(None, allow_none=True)
    drillup = Function(None, allow_none=True)
    drillupall = Function(None, allow_none=True)
    load = Function(None, allow_none=True)
    redraw = Function(None, allow_none=True)
    render = Function(None, allow_none=True)
    selection = Function(None, allow_none=True)
    selection = Function(None, allow_none=True)


class Events(HCBase):
    afterAnimate = Function(None, allow_none=True)
    checkboxClick = Function(None, allow_none=True)
    click = Function(None, allow_none=True)
    hide = Function(None, allow_none=True)
    legendItemClick = Function(None, allow_none=True)
    mouseOut = Function(None, allow_none=True)
    mouseOver = Function(None, allow_none=True)
    show = Function(None, allow_none=True)


class PlotEvents(HCBase):
    click = Function(None, allow_none=True)
    mouseover = Function(None, allow_none=True)
    mouseout = Function(None, allow_none=True)
    mousemove = Function(None, allow_none=True)


class PlotEvents2(PlotEvents):
    remove = Function(None, allow_none=True)
    select = Function(None, allow_none=True)
    unselect = Function(None, allow_none=True)
    update = Function(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class Point(HCBase):
    events = Instance(PlotEvents2, allow_none=True)
