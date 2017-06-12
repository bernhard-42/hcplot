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

from .types import Color
from .datalabels import DataLabels
from .events import PlotEvents2
from .position import XYFloat
from traitlets import Unicode, Bool, Integer, Instance, TraitType, Undefined


class SeriesData(XYFloat):
    className = Unicode(None, allow_none=True)
    color = Color(None, allow_none=True)
    colorIndex = Integer(None, allow_none=True)
    dataLabels = Instance(DataLabels, allow_none=True)
    description = Unicode(None, allow_none=True)
    drilldown = Unicode(None, allow_none=True)
    events = Instance(PlotEvents2, allow_none=True)
    id_ = Unicode(None, allow_none=True)
    labelrank = Integer(None, allow_none=True)
    name = Unicode(None, allow_none=True)
    selected = Bool(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class _SeriesData(TraitType):
    default_value = []
    info_text = 'SeriesData type or [number, ...] or [[number, number], ...]'

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        super(__class__, self).__init__(default_value=default_value,   # noqa F821
                                        allow_none=allow_none, **kwargs)

    def validate(self, obj, value):
        if isinstance(value, SeriesData) or isinstance(value, (tuple, list)):
            return value
        else:
            self.error(obj, value)
