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

from .data import Data
from .utils.helpers import update
from .base import Base


class Layer(Base):

    def __init__(self, dataOrConfigs, position, showLegend, **kwargs):

        # define all possible configs, ...
        self.mapping = {}
        self.scales = {}
        self.data = self.parseArgs(dataOrConfigs)

        self.position = position
        self.showLegend = showLegend
        for k, v in kwargs.items():
            setattr(self, k, v)

    def setFigure(self, figure):
        self.figure = figure
        self.layer = 1 + figure.layer
        self.usePlotLevel = figure.usePlotLevel.copy()

        # remember scales of this layer ...
        scales = self.scales

        # ... and merge mappings and config of the figure
        self.mapping = update(self.mapping, figure.mapping)
        self.scales = update(self.scales,  figure.scales)

        if self.data is None:
            # apply changes of mapping, scales to global data
            self.data = figure.data
            if self.mapping != {} or scales != {}:
                self.coding = self.createPlotConfig(self.mapping, scales, self.layer)
                for k, v in self.coding.items():
                    self.usePlotLevel[k] = v if isinstance(v, str) else "%s._%d" % (k, self.layer)
        else:
            self.data = Data(self.data)
            # apply merged mapping and scales to local data
            self.coding = self.createPlotConfig(self.mapping, self.scales, self.layer)
            for k, v in self.coding.items():
                self.usePlotLevel[k] = v if isinstance(v, str) else "%s._%d" % (k, self.layer)
