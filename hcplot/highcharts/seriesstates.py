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
from .animation import _Animation
from .marker import Marker
from traitlets import Dict, Float, Integer, Bool, Instance


class Halo(HCBase):
    attributes = Dict(None, allow_none=True)
    opacity = Float(None, allow_none=True)
    size = Integer(None, allow_none=True)


class Hover(HCBase):
    animation = _Animation(None, allow_none=True)
    enabled = Bool(None, allow_none=True)
    halo = Instance(Halo, allow_none=True)
    lineWidth = Integer(None, allow_none=True)
    lineWidthPlus = Integer(None, allow_none=True)
    marker = Instance(Marker, allow_none=True)


class SeriesStates(HCBase):
    hover = Instance(Hover, allow_none=True)
