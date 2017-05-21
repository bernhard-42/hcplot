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


import math
from ...utils.color import rgb2str


class D3Colors(object):
    """
    Source: http://d3js.org
    """
    categorialScheme = {
        "c10":  [( 31,119,180), (255,127, 14), ( 44,160, 44), (214, 39, 40), (148,103,189), (140, 86, 75), (227,119,194), (127,127,127), (188,189, 34), ( 23,190,207)],         # noqa E501,E231,E201
        "c20":  [( 31,119,180), (174,199,232), (255,127, 14), (255,187,120), ( 44,160, 44), (152,223,138), (214, 39, 40), (255,152,150), (148,103,189), (197,176,213),          # noqa E501,E231,E201
                 (140, 86, 75), (196,156,148), (227,119,194), (247,182,210), (127,127,127), (199,199,199), (188,189, 34), (219,219,141), ( 23,190,207), (158,218,229)],         # noqa E501,E231,E201
        "c20b": [( 57, 59,121), ( 82, 84,163), (107,110,207), (156,158,222), ( 99,121, 57), (140,162, 82), (181,207,107), (206,219,156), (140,109, 49), (189,158, 57),          # noqa E501,E231,E201
                 (231,186, 82), (231,203,148), (132, 60, 57), (173, 73, 74), (214, 97,107), (231,150,156), (123, 65,115), (165, 81,148), (206,109,189), (222,158,214)],         # noqa E501,E231,E201
        "c20c": [( 49,130,189), (107,174,214), (158,202,225), (198,219,239), (230, 85, 13), (253,141, 60), (253,174,107), (253,208,162), ( 49,163, 84), (116,196,118),          # noqa E501,E231,E201
                 (161,217,155), (199,233,192), (117,107,177), (158,154,200), (188,189,220), (218,218,235), ( 99, 99, 99), (150,150,150), (189,189,189), (217,217,217)],         # noqa E501,E231,E201
    }

    #
    # Get discrete results
    #

    @classmethod
    def _get(cls, scheme, color, size):
        colors = scheme.get(color)
        if colors is None:
            return []
        elif size is None:
            return colors
        elif size <= len(colors):
            return colors[:size]
        else:
            print("Warning: size too large for scheme, stacking largest color list to match size")
            factor = math.ceil(size / (len(colors)))
            return (colors * factor)[:size]

    #
    # Accessors
    #

    @classmethod
    def c10(cls, sizeOrSeries, asString=False):
        result = cls._get(cls.categorialScheme, "c10", size=sizeOrSeries)
        return rgb2str(result) if asString else result

    @classmethod
    def c20(cls, sizeOrSeries, asString=False):
        result = cls._get(cls.categorialScheme, "c20", size=sizeOrSeries)
        return rgb2str(result) if asString else result

    @classmethod
    def c20b(cls, sizeOrSeries, asString=False):
        result = cls._get(cls.categorialScheme, "c20b", size=sizeOrSeries)
        return rgb2str(result) if asString else result

    @classmethod
    def c20c(cls, sizeOrSeries, asString=False):
        result = cls._get(cls.categorialScheme, "c20c", size=sizeOrSeries)
        return rgb2str(result) if asString else result

    #
    # Info
    #

    @classmethod
    def info(cls):
        return list(cls.categorialScheme.keys())


#
# Quick Accessor
#

def getD3(typ, size):
    return getattr(D3Colors, typ)(size)
