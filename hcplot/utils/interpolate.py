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


def spline(values):
    """
    -------------------------------------------------------------------------
    Ported from https://github.com/d3/d3-interpolate/blob/master/src/basis.js
    Copyright 2010-2016 Mike Bostock
    License: https://github.com/d3/d3-interpolate/blob/master/LICENSE
    -------------------------------------------------------------------------
    """
    
    def basis(t1, v0, v1, v2, v3):
        t2 = t1 * t1
        t3 = t2 * t1
        return (   (1 - 3 * t1 + 3 * t2 -     t3) * v0   \
                 + (4 - 6 *          t2 + 3 * t3) * v1   \
                 + (1 + 3 * t1 + 3 * t2 - 3 * t3) * v2   \
                 +                            t3  * v3   \
               ) / 6

    def f(t, n):
        if t <= 0:
            i = t = 0
        elif t >= 1:
            i = n - 1
            t = 1
        else:
            i = math.floor(t * n)
        v1 = values[i]
        v2 = values[i + 1]
        v0 = values[i - 1] if i > 0     else 2 * v1 - v2
        v3 = values[i + 2] if i < n - 1 else 2 * v2 - v1

        return basis((t - i / n) * n, v0, v1, v2, v3)

    return lambda t: f(t, len(values) - 1)
