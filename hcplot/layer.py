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


class Layer(object):
    
    def __init__(self, data, mapping, scaleY, position, dropNa, showLegend, **kwargs):
        self.data = data
        self.mapping = mapping
        self.scaleY = scaleY
        self.position = position
        self.dropNa = dropNa
        self.showLegend = showLegend
        self.kwargs = kwargs
        
    def setFigure(self, figure):
        self.figure = figure

        # TODO: Does this make sense?
        # Inherit config from figure if not set explicitely in this layer
        for attr in ["data", "mapping", "scaleY"]:
            if getattr(self, attr) is None:
                setattr(self, attr, getattr(figure, attr))
        self.scaleX = figure.scaleX