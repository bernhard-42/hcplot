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
from sklearn.preprocessing import MinMaxScaler
from ..utils.helpers import reshape


class Alpha(object):

    #
    # Get interpolated results for non-discrete case
    #

    @classmethod
    def _interpolate(self, series, start, end):
        return MinMaxScaler([start, end]).fit_transform(reshape(series))

    #
    # Get discrete results
    #

    @classmethod
    def _get(cls, size, start, end):
        return np.linspace(start, end, size)

    #
    # Accessors
    #

    @classmethod
    def alpha(cls, sizeOrSeries, start=0.1, end=1.0):
        if isinstance(sizeOrSeries, int):
            return cls._get(size=sizeOrSeries, start=start, end=end)
        else:
            return cls._interpolate(series=sizeOrSeries, start=start, end=end)


#
# Quick Accessor
#

def getAlpha(size):
    return Alpha.alpha(size)
