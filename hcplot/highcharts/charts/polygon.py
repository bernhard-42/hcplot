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

from ..marker import Marker
from ..color import Color
from .base import SeriesBase4
from traitlets import Integer, Unicode, Instance


class PolygonOptions(SeriesBase4):
    type_ = Unicode("polygon", read_only=True)
    lineWidth = Integer(None, allow_none=True)
    dashStyle = Unicode(None, allow_none=True)
    turboThreshold = Integer(None, allow_none=True)
    cropThreshold = Integer(None, allow_none=True)
    negativeColor = Color(None, allow_none=True)
    marker = Instance(Marker, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class Polygon(PolygonOptions):
    type_ = Unicode("polygon", read_only=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821
