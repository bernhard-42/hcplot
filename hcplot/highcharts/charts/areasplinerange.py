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

from ..types import NumberOrString, Color
from .base import SeriesBase4
from traitlets import Integer, Unicode, Float, Bool


class AreaSplineRangeOptions(SeriesBase4):
    pointPlacement = NumberOrString(None, allow_none=True)
    lineWidth = Integer(None, allow_none=True)
    dashStyle = Unicode(None, allow_none=True)
    turboThreshold = Integer(None, allow_none=True)
    cropThreshold = Integer(None, allow_none=True)
    negativeColor = Color(None, allow_none=True)
    linecap = Unicode(None, allow_none=True)
    connectNulls = Bool(None, allow_none=True)
    fillColor = Color(None, allow_none=True)
    lineColor = Color(None, allow_none=True)
    fillOpacity = Float(None, allow_none=True)
    negativeFillColor = Color(None, allow_none=True)
    trackByArea = Bool(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class AreaSplineRange(AreaSplineRangeOptions):
    type_ = Unicode("areasplinerange", read_only=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821
