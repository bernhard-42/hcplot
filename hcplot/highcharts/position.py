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
from traitlets import Float, Integer, Unicode


class XYFloat(HCBase):
    x = Float(None, allow_none=True)
    y = Float(None, allow_none=True)


class XYInteger(HCBase):
    x = Integer(None, allow_none=True)
    y = Integer(None, allow_none=True)


class Position(XYFloat):
    align = Unicode(None, allow_none=True)
    verticalAlign = Unicode(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821
