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

from .scatter import Scatter


class Bubble(Scatter):

    def __init__(self, minSize=None, maxSize=None, zThreshold=None, displayNegative=None, sizeBy=None,
                 sizeByAbsoluteValue=None, zMax=None, zMin=None,
                 **kwargs):

        super(__class__, self).__init__(**kwargs)         # noqa F821

        params = {"minSize": minSize, "maxSize": maxSize, "zThreshold": zThreshold,
                  "displayNegative": displayNegative, "sizeBy": sizeBy,
                  "sizeByAbsoluteValue": sizeByAbsoluteValue, "zMax": zMax, "zMin": zMin}
        self.setIfExists(params)
