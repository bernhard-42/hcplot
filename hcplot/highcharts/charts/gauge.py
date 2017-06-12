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

from ..dial import Dial, Pivot
from ..color import Color
from .base import GaugeBase
from traitlets import Bool, Integer, Instance, Unicode


class GaugeOptions(GaugeBase):
    enableMouseTracking = Bool(None, allow_none=True)
    colorIndex = Integer(None, allow_none=True)
    negativeColor = Color(None, allow_none=True)
    dial = Instance(Dial, allow_none=True)
    pivot = Instance(Pivot, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class Gauge(GaugeOptions):
    type_ = Unicode("gauge", read_only=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821
