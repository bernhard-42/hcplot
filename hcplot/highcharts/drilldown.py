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
from .types import CSSObject
from .animation import _Animation
from .position import Position
from .buttons import SvgButtonTheme
from .series import SeriesOptions
from traitlets import Unicode, Bool, Instance, List


class DrillUpButton(HCBase):
    position = Instance(Position, allow_none=True)
    relativeTo = Unicode(None, allow_none=True)
    theme = Instance(SvgButtonTheme, allow_none=True)


class DrillDown(HCBase):
    activeAxisLabelStyle = CSSObject(None, allow_none=True)
    activeDataLabelStyle = CSSObject(None, allow_none=True)
    allowPointDrilldown = Bool(None, allow_none=True)
    animation = _Animation(None, allow_none=True)
    drillUpButton = Instance(DrillUpButton, allow_none=True)
    series = List(SeriesOptions, allow_none=True)
