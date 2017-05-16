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
from ..components import Components


class Points(Layer):

    def __init__(self, data=None, mapping=None, scales=None, position=None, dropNa=False, showLegend=False, color=None, size=None, shape=None):
        super(__class__, self).__init__(data, mapping, scales, position, dropNa, showLegend, color=color, size=size, shape=shape)
        self.options = { "type": "scatter", "marker": {"radius": 2 if size is None else size}}

        
    def prepareData(self, df, mx, my):
        mapping = {"x":mx, "y":my}
        for k,v in self.mapping.items():
            if k not in ["x", "y"] and v is not None:
                mapping[k] = v
        names = list(mapping.keys())
        cols = list(mapping.values())
                
        if df.shape[0] > self.figure.performanceTreshold:
            df2 = df[cols]
            return df2.to_dict("split")["data"]
        else:
            df2 = df[cols].copy()
            df2.columns = names

            for attr in ["color", "shape", "size"]:
                if attr in names:
                    df2[attr] = df2[attr].astype('category')
                    count = df2[attr].cat.categories.size
                    df2[attr] = df2[attr].cat.rename_categories(self.scales[attr](count))

            data = df2.to_dict("split")["data"]

            result = [Components.point(names, values) for values in data]

            return result
        