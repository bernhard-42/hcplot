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

from .color import ColorBrewer, D3Colors
from .shape import Shape as ShapeClass
import numpy as np


class Alpha(object):

    def __init__(self, discrete=True):
        self.discrete = discrete

    def get(self):
        if self.discrete:
            return lambda size: list(np.linspace(0.0, 1.0, size + 2))[1:-1]
        else:
            def conv(array):
                if len(array) == 0:
                    return []

                mina = min(array)
                d = max(array) - mina
                if d == 0:
                    return [0.5] * len(array)
                else:
                    l = 1 / len(array)
                    f = (1 - 2 * l) / d
                    b = (l - f * mina)
                    result = [b + f * a for a in array]

                return result

            return lambda array: conv(array)


class D3(object):

    def __init__(self, typ):
        self.discrete = True
        self.typ = typ

    def get(self):
        return getattr(D3Colors, self.typ)


class Brewer(object):

    def __init__(self, typ, palette, discrete=True):
        self.typ = typ
        self.palette = palette
        self.discrete = discrete

    def get(self):
        if self.typ == "qual":
            assert self.discrete, "Qualitative palette cannot be used for non discrete data"
            return lambda size: getattr(ColorBrewer, self.typ)(self.palette, size=size)
        else:
            if self.discrete:
                return lambda size: getattr(ColorBrewer, self.typ)(self.palette, True, size=size)
            else:
                def conv(array):
                    mina = min(array)
                    d = max(array) - mina
                    if d == 0:
                        return getattr(ColorBrewer, self.typ)(self.palette, size=1) * len(array)
                    else:
                        scaledArray = [(a - mina) / d for a in array]
                        return getattr(ColorBrewer, self.typ)(self.palette, False,
                                                              array=scaledArray)

                return lambda array: conv(array)


class Gradient(object):

    def __init__(self, typ):
        self.discrete = True
        self.typ = typ


class Grey(object):

    def __init__(self, discrete=True):
        self.discrete = discrete


class Hue(object):

    def __init__(self, discrete=True):
        self.discrete = discrete


class Size(object):

    def __init__(self, discrete=True):
        self.discrete = discrete


class Shape(object):

    def __init__(self, discrete=True):
        self.discrete = discrete


class X(object):

    def __init__(self, func=None, reverse=False, discrete=True):
        self.discrete = discrete
        self.reverse = reverse
        self.func = func


class Y(object):

    def __init__(self, func=None, reverse=False, discrete=True):
        self.discrete = discrete
        self.reverse = reverse
        self.func = func


def shapes():
    return ShapeClass.get


def defaultScale():
    return {"color": Brewer("qual", "Accent"), "shape": shapes()}


def identity():
    return 1


def manual(obj):
    return obj
