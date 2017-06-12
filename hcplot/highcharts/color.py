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
from ..utils.color import web2rgba
from traitlets import TraitType, Undefined, Float, Instance, List


class Color(TraitType):
    """A color trait."""

    default_value = "rgba(124,181,236,1.0)"
    info_text = 'an rgba color'

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        super(__class__, self).__init__(default_value=default_value,          # noqa F821
                                        allow_none=allow_none, **kwargs)

    def validate(self, obj, value):
        if isinstance(value, tuple) and (len(value) == 3 or len(value) == 4):
            return value
        else:
            try:
                rgba = web2rgba(value)
                return rgba
            except Exception:
                self.error(obj, value)

    @staticmethod
    def conv(value):
        return "rgba(%d,%d,%d,%5.3f)" % value


class LinearGradient(HCBase):
    x1 = Float(0.0, allow_none=False)
    x2 = Float(0.0, allow_none=False)
    y1 = Float(1.0, allow_none=False)
    y2 = Float(1.0, allow_none=False)


class RadialGradient(HCBase):
    cx = Float(0.0, allow_none=False)
    cy = Float(0.0, allow_none=False)
    r = Float(1.0, allow_none=False)


class GradientStop(HCBase):
    stop = Float(None, allow_none=True)
    color = Color(None, allow_none= True)

    @staticmethod
    def conv(value):
        return (value["stop"], value["color"])


class FillColor(HCBase):
    linearGradient = Instance(LinearGradient, allow_none=True)
    radialGradient = Instance(RadialGradient, allow_none=True)
    stops = List(Instance(GradientStop, allow_none=True))


class _FillColor(TraitType):
    default_value = "rgba(124,181,236,1.0)"
    info_text = 'FillColor Object or Color Object'

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        super(__class__, self).__init__(default_value=default_value,          # noqa F821
                                        allow_none=allow_none, **kwargs)

    def validate(self, obj, value):
        if (isinstance(value, tuple) and (len(value) == 3 or len(value) == 4)) or \
           isinstance(value, FillColor):
            return value
        else:
            try:
                rgba = web2rgba(value)
                return rgba
            except Exception:
                self.error(obj, value)

    @staticmethod
    def conv(value):
        if isinstance(value, (list, tuple)):
            return "rgba(%d,%d,%d,%5.3f)" % value
        else:
            return value
