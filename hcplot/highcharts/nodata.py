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
from .position import Position
from traitlets import Bool, Instance, Dict


class NoData(HCBase):
    attr = Dict(None, allow_none=True)
    position = Instance(Position, allow_none=True)
    style = CSSObject(None, allow_none=True)
    useHTML = Bool(None, allow_none=True)