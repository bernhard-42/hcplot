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
from .types import NumberOrString, IntegerOrPercentageString
from traitlets import Instance, Unicode, List, Integer


class PaneBackground(HCBase):
    backgroundColor = Color(None, allow_none=True)
    borderColor = Color(None, allow_none=True)
    borderWidth = Integer(None, allow_none=True)
    className = Unicode(None, allow_none=True)
    innerRadius = NumberOrString(None, allow_none=True)
    outerRadius = NumberOrString(None, allow_none=True)
    shape = Unicode(None, allow_none=True)


class Pane(HCBase):
    background = List(Instance(PaneBackground))
    center = List(IntegerOrPercentageString(), maxLen=2)
    endAngle = Integer(None, allow_none=True)
    size = IntegerOrPercentageString(None, allow_none=True)
    startAngle = Integer(None, allow_none=True)
