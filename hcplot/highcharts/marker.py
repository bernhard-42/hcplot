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
from .color import Color, _FillColor
from traitlets import Integer, Instance, Bool, Unicode, Float


class MarkerSelect(HCBase):
    enabled = Bool(None, allow_none=True)
    fillColor = _FillColor(None, allow_none=True)
    lineColor = Color(None, allow_none=True)
    lineWidth = Integer(None, allow_none=True)
    radius = Integer(None, allow_none=True)


class MarkerHover(MarkerSelect):
    lineWidthPlus = Integer(None, allow_none=True)
    radiusPlus = Integer(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class MarkerStates(HCBase):
    hover = Instance(MarkerHover, allow_none=True)
    select = Instance(MarkerSelect, allow_none=True)


class Marker(HCBase):
    enabled = Bool(None, allow_none=True)
    fillColor = _FillColor(None, allow_none=True)
    height = Integer(None, allow_none=True)
    lineColor = Color(None, allow_none=True)
    lineWidth = Integer(None, allow_none=True)
    radius = Float(None, allow_none=True)
    states = Instance(MarkerStates, allow_none=True)
    symbol = Unicode(None, allow_none=True)
    width = Integer(None, allow_none=True)
