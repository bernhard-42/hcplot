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

import pandas as pd
from .utils import Config


class Layer(object):
    
    def __init__(self, dataOrConfigs, position, showLegend, **kwargs):

        # define all possible configs, ...
        self.df = None
        self.mapping = None
        self.scales = None
        
        
        # ... get data and all provided configs ...
        for dataOrConfig in dataOrConfigs:
            if isinstance(dataOrConfig, pd.DataFrame):
                self.df = dataOrConfig
            else:
                assert isinstance(dataOrConfig, Config), "Only Config objects allowed as positional arguments"
                setattr(self, dataOrConfig.param, dataOrConfig.config)

        self.position = position
        self.showLegend = showLegend
        for k,v in kwargs.items():
            setattr(self, k, v)
        
    def setFigure(self, figure):
        self.figure = figure
        self.layer = 1 + figure.layer
        self.usePlotLevel = figure.usePlotLevel
        
        if self.mapping is not None or self.scales is not None:
            if self.mapping is None:
                self.mapping = figure.mapping

            self.coding = figure.createPlotConfig(self.mapping, self.scales, self.layer)
            for k,v in self.coding.items():
                self.usePlotLevel[k] = "%s._%d" % (k, self.layer)
