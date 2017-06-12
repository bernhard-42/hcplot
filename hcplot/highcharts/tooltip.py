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
from .types import CSSObject, Function
from .color import Color
from .crosshair import _CrossHair
from traitlets import Unicode, Bool, Integer, Dict


class SeriesTooltip(HCBase):
    dateTimeLabelFormats = Dict(None, allow_none=True)
    followPointer = Bool(None, allow_none=True)
    followTouchMove = Bool(None, allow_none=True)
    footerFormat = Unicode(None, allow_none=True)
    headerFormat = Unicode(None, allow_none=True)
    hideDelay = Integer(None, allow_none=True)
    padding = Integer(None, allow_none=True)
    pointFormat = Unicode(None, allow_none=True)
    pointFormatter = Function(None, allow_none=True)
    split = Bool(None, allow_none=True)
    valuePrefix = Unicode(None, allow_none=True)
    valueSuffix = Unicode(None, allow_none=True)
    xDateFormat = Unicode(None, allow_none=True)


class Tooltip(SeriesTooltip):
    animation = Bool(None, allow_none=True)
    backgroundColor = Color(None, allow_none=True)
    borderColor = Color(None, allow_none=True)
    borderRadius = Integer(None, allow_none=True)
    borderWidth = Integer(None, allow_none=True)
    crosshairs = _CrossHair(None, allow_none=True)
    enabled = Bool(None, allow_none=True)
    formatter = Function(None, allow_none=True)
    positioner = Function(None, allow_none=True)
    shadow = Bool(None, allow_none=True)
    shape = Unicode(None, allow_none=True)
    shared = Bool(None, allow_none=True)
    snap = Integer(None, allow_none=True)
    style = CSSObject(None, allow_none=True)
    useHTML = Bool(None, allow_none=True)
    valueDecimals = Integer(None, allow_none=True)
