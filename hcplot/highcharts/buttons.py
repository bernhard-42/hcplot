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
from .types import Function, NumberOrString, IntegerOrPercentageString
from .color import Color
from .position import Position
from traitlets import Unicode, Bool, Instance, List, Integer, Float


class MenuItem(HCBase):
    text = Unicode(None, allow_none=True)
    onclick = Function(None, allow_none=True)


class SvgTheme(HCBase):
    fill = Unicode(None, allow_none=True)
    fill_opacity = Float(None, allow_none=True)
    fill_rule = NumberOrString(None, allow_none=True)
    stroke = Unicode(None, allow_none=True)
    stroke_width = Integer(None, allow_none=True)
    stroke_dasharray = Unicode(None, allow_none=True)
    stroke_dashoffset = IntegerOrPercentageString(None, allow_none=True)
    stroke_linecap = Unicode(None, allow_none=True)
    stroke_linejoin = Unicode(None, allow_none=True)
    stroke_miterlimit = Integer(None, allow_none=True)
    stroke_opacity = Float(None, allow_none=True)
    r = Integer(None, allow_none=True)
    style = Unicode(None, allow_none=True)


class ButtonStates(HCBase):
    hover = Instance(SvgTheme, allow_none=True)
    select = Instance(SvgTheme, allow_none=None)


class SvgButtonTheme(SvgTheme):
    states = Instance(ButtonStates, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class ButtonOptions(HCBase):
    align = Unicode(None, allow_none=True)
    enabled = Bool(None, allow_none=True)
    height = Integer(None, allow_none=True)
    symbolFill = Color(None, allow_none=True)
    symbolSize = Integer(None, allow_none=True)
    symbolStroke = Color(None, allow_none=True)
    symbolStrokeWidth = Integer(None, allow_none=True)
    symbolX = Float(None, allow_none=True)
    symbolY = Float(None, allow_none=True)
    text = Unicode(None, allow_none=True)
    theme = Instance(SvgButtonTheme, allow_none=True)
    verticalAlign = Unicode(None, allow_none=True)
    width = Integer(None, allow_none=True)
    y = Integer(None, allow_none=True)


class ContextButtons(ButtonOptions):
    menuItems = List(Instance(MenuItem))
    onclick = Function(None, allow_none=True)
    symbol = Unicode(None, allow_none=True)
    x = Integer(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class Buttons(HCBase):
    buttons = Instance(ContextButtons, allow_none=True)


class ResetZoomButton(HCBase):
    position = Instance(Position, allow_none=True)
    relativeTo = Unicode(None, allow_none=True)
    theme = Instance(SvgButtonTheme, allow_none=True)
