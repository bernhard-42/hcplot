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

from ..datalabels import Level
from .base import MapBase
from traitlets import Bool, Unicode, List, Integer, Instance, Float


class TreeMapOptions(MapBase):
    interactByLeaf = Bool(None, allow_none=True)
    layoutAlgorithm = Unicode(None, allow_none=True)
    layoutStartingDirection = Unicode(None, allow_none=True)
    levelIsConstant = Bool(None, allow_none=True)
    levels = List(Instance(Level))
    opacity = Float(None, allow_none=True)
    sortIndex = Integer(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class TreeMap(TreeMapOptions):
    type_ = Unicode("treemap", read_only=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821
