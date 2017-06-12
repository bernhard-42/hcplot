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
from .types import Function
from .chart import ChartOptions
from traitlets import Instance, List, Integer


class ResponsiveConditon(HCBase):
    callback = Function(None, allow_none=True)
    maxHeight = Integer(None, allow_none=True)
    maxWidth = Integer(None, allow_none=True)
    minHeight = Integer(None, allow_none=True)
    minWidth = Integer(None, allow_none=True)


class ResponsiveRule(HCBase):
    chartOptions = Instance(ChartOptions, allow_none=True)
    condition = Instance(ResponsiveConditon, allow_none=True)


class Responsive(HCBase):
    rules = List(Instance(ResponsiveRule))


class ChartOptionsResponsive(ChartOptions):
    responsive = Instance(Responsive, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821
