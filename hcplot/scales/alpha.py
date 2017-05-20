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


import numpy as np


class Alpha(object):

    #
    # Get interpolated results for non-discrete case
    #

    @classmethod
    def _interpolate(self, array):
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
            return [b + f * a for a in array]

    #
    # Get discrete results
    #

    @classmethod
    def _get(cls, size):
        return list(np.linspace(0.0, 1.0, size + 2))[1:-1]

    #
    # Accessors
    #

    @classmethod
    def alpha(cls, discrete=True, size=None, array=None):
        if discrete:
            return cls._get(size)
        else:
            return cls._interpolate(array)


#
# Quick Accessor
#

def alpha(size):
    return Alpha.alpha(size)
