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
from .buttons import Buttons
from .chart import ChartOptions
from traitlets import Unicode, Bool, Instance, Integer, Float, Dict


class Exporting(HCBase):
    allowHTML = Bool(None, allow_none=True)
    buttons = Instance(Buttons, allow_none=True)
    chartOptions = Instance(ChartOptions, allow_none=True)  # TODO
    enabled = Bool(None, allow_none=True)
    error = Function(None, allow_none=True)
    fallbackToExportServer = Bool(None, allow_none=True)
    filename = Unicode(None, allow_none=True)
    formAttributes = Dict(None, allow_none=True)
    libURL = Unicode(None, allow_none=True)
    printMaxWidth = Integer(None, allow_none=True)
    scale = Float(None, allow_none=True)
    sourceHeight = Integer(None, allow_none=True)
    sourceWidth = Integer(None, allow_none=True)
    type = Unicode(None, allow_none=True)
    url = Unicode(None, allow_none=True)
    width = Integer(None, allow_none=True)
