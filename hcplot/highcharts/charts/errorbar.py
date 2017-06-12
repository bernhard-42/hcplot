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

from ..color import Color
from .base import SeriesBase3
from traitlets import Unicode, Float, List, Integer, Bool


class ErrorBarOptions(SeriesBase3):
    type_ = Unicode("errorbar", read_only=True)
    pointIntervalUnit = Unicode(None, allow_none=True)
    pointStart = Float(None, allow_none=True)
    pointInterval = Float(None, allow_none=True)
    pointPlacement = Float(None, allow_none=True)
    colors = List(Color(allow_none=True))
    depth = Integer(None, allow_none=True)
    colorByPoint = Bool(None, allow_none=True)
    crisp = Bool(None, allow_none=True)
    lineWidth = Integer(None, allow_none=True)
    turboThreshold = Integer(None, allow_none=True)
    negativeColor = Color(None, allow_none=True)
    maxPointWidth = Integer(None, allow_none=True)
    edgeColor = Color(None, allow_none=True)
    edgeWidth = Integer(None, allow_none=True)
    groupZPadding = Integer(None, allow_none=True)
    pointPadding = Integer(None, allow_none=True)
    pointRange = Float(None, allow_none=True)
    pointWidth = Float(None, allow_none=True)
    stemColor = Color(None, allow_none=True)
    stemDashStyle = Unicode(None, allow_none=True)
    stemWidth = Integer(None, allow_none=True)
    whiskerColor = Color(None, allow_none=True)
    whiskerLength = Integer(None, allow_none=True)
    whiskerWidth = Integer(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class ErrorBar(ErrorBarOptions):
    type_ = Unicode("errorbar", read_only=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821
