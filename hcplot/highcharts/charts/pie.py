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

from ..animation import _Animation
from ..types import IntegerOrPercentageString
from .base import SeriesBase5
from traitlets import Float, Unicode


class PieOptions(SeriesBase5):
    animation = _Animation(None, allow_none=True)
    startAngle = Float(None, allow_none=True)
    endAngle = Float(None, allow_none=True)
    innerSize = IntegerOrPercentageString(None, allow_none=True)
    size = IntegerOrPercentageString(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class Pie(PieOptions):
    type_ = Unicode("pie", read_only=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821
