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
from .types import Color, CSSObject
from .shadow import _Shadow
from .position import XYFloat
from .events import Function
from traitlets import Float, Integer, Unicode, Bool, Instance


class DataLabels(XYFloat):
    align = Unicode(None, allow_none=True)
    allowOverlap = Bool(None, allow_none=True)
    backgroundColor = Color(None, allow_none=True)
    borderColor = Color(None, allow_none=True)
    borderRadius = Integer(None, allow_none=True)
    borderWidth = Integer(None, allow_none=True)
    className = Unicode(None, allow_none=True)
    color = Color(None, allow_none=True)
    crop = Bool(None, allow_none=True)
    defer = Bool(None, allow_none=True)
    enabled = Bool(None, allow_none=True)
    format_ = Unicode(None, allow_none=True)
    formatter = Function(None, allow_none=True)
    inside = Bool(None, allow_none=True)
    overflow = Unicode(None, allow_none=True)
    padding = Integer(None, allow_none=True)
    rotation = Float(None, allow_none=True)
    shadow = _Shadow(None, allow_none=True)
    shape = Unicode(None, allow_none=True)
    style = CSSObject(None, allow_none=True)
    useHTML = Bool(None, allow_none=True)
    verticalAlign = Unicode(None, allow_none=True)
    zIndex = Integer(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class Level(HCBase):
    borderColor = Color(None, allow_none=True)
    borderDashStyle = Unicode(None, allow_none=True)
    borderWidth = Integer(None, allow_none=True)
    color = Color(None, allow_none=True)
    dataLabels = Instance(DataLabels, allow_none=True)
    layoutAlgorithm = Unicode(None, allow_none=True)
    layoutStartingDirection = Unicode(None, allow_none=True)
    level = Integer(None, allow_none=True)
