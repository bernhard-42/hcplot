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
from traitlets import TraitType, Integer, Unicode, Undefined, Bool
from .color import Color


class CrossHair(HCBase):
    className = Unicode(None, allow_none=True)
    color = Color(None, allow_none=True)
    dashStyle = Unicode(None, allow_none=True)
    snap = Bool(None, allow_none=True)
    width = Integer(None, allow_none=True)
    zIndex = Integer(None, allow_none=True)


class _CrossHair(TraitType):
    info_text = 'Bool or an CrossHair object'

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        super(__class__, self).__init__(default_value=default_value,          # noqa F821
                                        allow_none=allow_none, **kwargs)

    def validate(self, obj, value):
        if isinstance(value, type(True)) or isinstance(value, CrossHair):
            return value
        else:
            self.error(obj, value)
