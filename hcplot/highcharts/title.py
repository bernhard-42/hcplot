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

from .types import CSSObject
from .position import XYInteger
from traitlets import Unicode, Bool, Integer


class SubTitle(XYInteger):
    align = Unicode(None, allow_none=True)
    floating = Bool(None, allow_none=True)
    style = CSSObject(None, allow_none=True)
    text = Unicode(None, allow_none=True)
    useHTML = Bool(None, allow_none=True)
    verticalAlign = Unicode(None, allow_none=True)
    widthAdjust = Integer(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class Title(SubTitle):
    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821
