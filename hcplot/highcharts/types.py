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

from traitlets import TraitType, Undefined
from ..utils.color import web2rgba


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


class Function(TraitType):
    """A Javascript Function trait."""

    default_value = "function() {}"
    info_text = 'string representation of a javascript function'

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        super(__class__, self).__init__(default_value=default_value,          # noqa F821
                                        allow_none=allow_none, **kwargs)

    def validate(self, obj, value):
        if isinstance(value, str) and value.startswith("function()"):
            return value
        else:
            self.error(obj, value)


class CSSObject(TraitType):
    """A CSS trait."""

    default_value = {}
    info_text = 'a CSS dict {"key": value, ...}'

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        super(__class__, self).__init__(default_value=default_value,          # noqa F821
                                        allow_none=allow_none, **kwargs)

    def validate(self, obj, value):
        if isinstance(value, dict):
            return value
        else:
            self.error(obj, value)


class SVGObject(TraitType):
    """A CSS trait."""

    default_value = {}
    info_text = 'a SVG dict {"key": value, ...}'

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        super(__class__, self).__init__(default_value=default_value,          # noqa F821
                                        allow_none=allow_none, **kwargs)

    def validate(self, obj, value):
        if isinstance(value, dict):
            return value
        else:
            self.error(obj, value)


class BoolOrString(TraitType):
    default_value = True
    info_text = 'Bool or String'

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        super(__class__, self).__init__(default_value=default_value,          # noqa F821
                                        allow_none=allow_none, **kwargs)

    def validate(self, obj, value):
        if isinstance(value, type(True)) or isinstance(value, str):
            return value
        else:
            self.error(obj, value)


class NumberOrString(TraitType):
    default_value = True
    info_text = 'Number or String'

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        super(__class__, self).__init__(default_value=default_value,          # noqa F821
                                        allow_none=allow_none, **kwargs)

    def validate(self, obj, value):
        if type(value) in [int, float] or isinstance(value, str):
            return value
        else:
            self.error(obj, value)


class FloatOrAuto(TraitType):
    default_value = True
    info_text = 'Number or String "auto"'

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        super(__class__, self).__init__(default_value=default_value,          # noqa F821
                                        allow_none=allow_none, **kwargs)

    def validate(self, obj, value):
        if type(value) in [int, float] or value == "auto":
            return value
        else:
            self.error(obj, value)


class IntegerOrPercentageString(TraitType):
    default_value = "50%"
    info_text = 'Integer or PercentageString("50%")'

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        super(__class__, self).__init__(default_value=default_value,          # noqa F821
                                        allow_none=allow_none, **kwargs)

    def validate(self, obj, value):
        if isinstance(value, int) or (isinstance(value, str) and value[-1] == "%"):
            return value
        else:
            self.error(obj, value)
