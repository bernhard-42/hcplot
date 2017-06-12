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

from ..types import Color
from .columnrange import ColumnRangeOptions
from traitlets import Integer, Unicode


class ColumnOptions(ColumnRangeOptions):
    cropThreshold = Integer(None, allow_none=True)
    negativeColor = Color(None, allow_none=True)
    stack = Unicode(None, allow_none=True)
    stacking = Unicode(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class Column(ColumnOptions):
    type_ = Unicode("column", read_only=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821
