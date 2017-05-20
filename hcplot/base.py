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
from .config import Config
from .utils.color import rgb2str
from operator import itemgetter


class Base(object):

    def parseArgs(self, dataOrConfigs):

        # ... get all provided configs ...
        data = None
        for dataOrConfig in dataOrConfigs:
            if isinstance(dataOrConfig, pd.DataFrame):
                data = dataOrConfig

            elif isinstance(dataOrConfig, dict):
                data = pd.DataFrame(dataOrConfig)

            else:
                assert isinstance(dataOrConfig, Config), \
                    "Only Config objects (multiple) or DataFrame / column data dict (one) " + \
                    "allowed as positional arguments"
                getattr(self, dataOrConfig.param).update(dataOrConfig.config)

        return data

    def getMinMax(self, xScaleFree, yScaleFree):
        xmin = ymin = xmax = ymax = None

        if not (xScaleFree and yScaleFree):

            if isinstance(self.mapping["x"], (list, tuple)):
                allCols = list(set(self.mapping["x"]).union(set(self.mapping["y"])))
                minMax = [self.data.getMinMax(col) for col in allCols]
                if not xScaleFree:
                    xmin = ymin = min(minMax, key=itemgetter(0))[0]
                if not yScaleFree:
                    xmax = ymax = max(minMax, key=itemgetter(1))[1]

            else:
                if not xScaleFree:
                    xmin, xmax = self.data.getMinMax(self.mapping["x"])
                if not yScaleFree:
                    ymin, ymax = self.data.getMinMax(self.mapping["y"])

        return xmin, ymin, xmax, ymax

    def createPlotConfig(self, mapping, scales, layer):
        coding = {}
        for attr, name in mapping.items():
            layerAttr = "%s._%d" % (attr, layer)

            if name is not None and attr not in ["x", "y"] and scales.get(attr) is not None:
                if scales[attr] == 1:
                    coding[attr] = name
                else:
                    df = self.data.df
                    df[layerAttr] = df[name].astype("category")
                    count = df[layerAttr].cat.categories.size
                    scaleFunc = scales[attr].get()
                    if scales[attr].discrete:
                        newValues = scaleFunc(count)
                        if attr == "color":
                            newValues = rgb2str(newValues)
                        coding[attr] = zip(df[layerAttr].cat.categories, newValues)
                        df[layerAttr] = df[layerAttr].cat.rename_categories(newValues)
                    else:
                        newValues = scaleFunc(df[name])
                        if attr == "color":
                            newValues = rgb2str(newValues)
                        df[layerAttr] = newValues
                        coding[attr] = scaleFunc

        return coding
