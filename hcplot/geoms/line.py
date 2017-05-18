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


from ..layer import Layer

class Line(Layer):

    def __init__(self, *dataOrConfigs, 
                 position=None, showLegend=False, color=None, lineType="Solid", lineWidth=2, showMarker=None, marker="diamond"):
        super(__class__, self).__init__(dataOrConfigs, position, showLegend, color=color, lineType=lineType, showMarker=showMarker, marker=marker)
        self.options = { "type": "line", "dashStyle": lineType, "lineWidth": lineWidth } 
        
        if color is not None:
            self.options["color"] = color

        self.options["marker"] = { "symbol": marker }

        if showMarker is not None:
            self.options["marker"]["enabled"] = showMarker

        
    def prepareData(self, df, mx, my):
        return df[[mx, my]].to_dict("split")["data"]
