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


from ...utils.color import hcl2rgb, rgb2str
import numpy as np


class HueColors(object):
    """
    "Escaping RGBland: Selecting Colors for Statistical Graphics"
        Achim Zeileis, Wirtschaftsuniversität Wien
        Kurt Hornik, Wirtschaftsuniversität Wien
        Paul Murrell, The University of Auckland

    https://eeecon.uibk.ac.at/~zeileis/papers/Zeileis+Hornik+Murrell-2009.pdf
    """

    #
    # Accessors
    #

    @classmethod
    def qual(cls, h=(0, 360), c=100, l=65, sizeOrSeries=5, asString=False):
        size = sizeOrSeries if isinstance(sizeOrSeries, int) else (len(sizeOrSeries))

        d = (h[1] - h[0]) // (size - 1)
        result = [hcl2rgb(h[0] + d * i, c, l) for i in range(size)]
        return rgb2str(result) if asString else result

    @classmethod
    def seq(cls, h=260, c=(30, 90), l=(30, 90), fl=None, fc=None, sizeOrSeries=5, asString=False):
        size = sizeOrSeries if isinstance(sizeOrSeries, int) else (len(sizeOrSeries))

        if isinstance(c, int):
            crange = [c] * size
        else:
            if fc is None:
                crange = np.linspace(c[0], c[1], size)
            else:
                d = c[0] - c[1]
                crange = [c[1] + d * fc(x) for x in np.linspace(1, 0, size)]

        if isinstance(l, int):
            lrange = [l] * size
        else:
            if fl is None:
                lrange = np.linspace(l[0], l[1], size)
            else:
                d = l[0] - l[1]
                lrange = [l[1] + d * fl(x) for x in np.linspace(1, 0, size)]

        return [hcl2rgb(h, ci, li) for ci, li in zip(crange, lrange)]

    @classmethod
    def div(cls, h=[260, 0], c=(100, 0, 100), l=(30, 90, 30), fc=None, fl=None,
            sizeOrSeries=7, asString=False):

        size = sizeOrSeries if isinstance(sizeOrSeries, int) else (len(sizeOrSeries))

        s = size // 2 + 1
        return cls.seq(h[0], c[:2], l[:2], fc=fc, fl=fl, sizeOrSeries=s)[:-1] + \
            list(reversed(cls.seq(h[1], (c[2], c[1]), (l[2], l[1]), sizeOrSeries=s, fc=fc, fl=fl)))

    #
    # Info
    #

    @classmethod
    def info(cls):
        pass

    @classmethod
    def toDF(cls, typ):
        pass


#
# Quick Accessor
#

def getBrewer(typ, palette, size):
    return getattr(HueColors, typ)(palette, size)
