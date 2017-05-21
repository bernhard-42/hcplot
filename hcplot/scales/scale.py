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


from .colors.brewer import ColorBrewer
from .colors.d3 import D3Colors
from .shape import Shape as ShapeClass
from .alpha import Alpha as AlphaClass
from .size import Size as SizeClass


class Scale(object):

    def _accessor(self, cls, accessor, kwargs):
        self.method = getattr(cls, accessor)
        self.kwargs = kwargs

    def __call__(self, sizeOrSeries):
        return self.method(**self.kwargs, sizeOrSeries=sizeOrSeries)


class Alpha(Scale):

    def __init__(self, discrete=True):
        self.discrete = discrete
        self._accessor(AlphaClass, "alpha", {})


class D3(Scale):

    def __init__(self, typ, asString=True):
        self.discrete = True
        self._accessor(D3Colors, typ, {"asString": asString})

    @classmethod
    def info(cls):
        return D3Colors.info()


class Brewer(Scale):

    def __init__(self, typ, palette, discrete=True, asString=True):
        self.discrete = discrete
        self._accessor(ColorBrewer, typ, {"palette": palette, "asString": asString})

    @classmethod
    def info(cls):
        return ColorBrewer.info()


class Shape(Scale):

    def __init__(self):
        self.discrete = True
        self._accessor(ShapeClass, "shape", {})

    @classmethod
    def info(cls):
        return ShapeClass.info()


class Size(Scale):

    def __init__(self, start=2, end=20, incr=2, discrete=True):
        self.discrete = discrete
        self._accessor(SizeClass, "size", {"start": start, "end": end, "incr": incr})










class Gradient(object):

    # TODO

    def __init__(self, typ):
        self.discrete = True
        self.typ = typ


class Grey(object):

    # TODO

    def __init__(self, discrete=True):
        self.discrete = discrete


class Hue(object):

    # TODO

    def __init__(self, discrete=True):
        self.discrete = discrete


class X(object):

    # TODO

    def __init__(self, func=None, reverse=False, discrete=True):
        self.discrete = discrete
        self.reverse = reverse
        self.func = func


class Y(object):

    # TODO

    def __init__(self, func=None, reverse=False, discrete=True):
        self.discrete = discrete
        self.reverse = reverse
        self.func = func


def defaultScale():
    return {"color": Brewer("qual", "Accent"), "shape": Shape(), "alpha": Alpha(), "size": Size()}


def identity():
    return 1


def manual(obj):
    return obj