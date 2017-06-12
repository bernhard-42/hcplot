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
from .color import Color
from traitlets import Integer, Unicode


class Pivot(HCBase):
    backgroundColor = Color(None, allow_none=True)
    borderColor = Color(None, allow_none=True)
    borderWidth = Integer(None, allow_none=True)
    radius = Unicode(None, allow_none=True)


class Dial(Pivot):
    baseLength = Unicode(None, allow_none=True)
    baseWidth = Integer(None, allow_none=True)
    rearLength = Unicode(None, allow_none=True)
    topWidth = Integer(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821
