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


import os
import json
import datetime
import numpy as np
import pandas as pd

from IPython.display import HTML, Javascript, display

from .scale import brewer, d3, shapes


def loadLibraries():
    folder = os.path.dirname(__file__)
    
    with open(os.path.join(folder, "./css", "styles.css"), "r") as fd:
        css = fd.read()
    display(HTML("<style>%s</style>" % css))
 
    with open(os.path.join(folder, "./js", "load.js"), "r") as fd:
        js = fd.read()
    display(Javascript(js))


class ScipyEncoder(json.JSONEncoder):
    def default(self, o):

        if isinstance(o, pd.tslib.Timestamp):
            o = o.to_pydatetime()
            
        if isinstance(o, datetime.datetime):
            return int(o.timestamp() * 1000)
        
        if isinstance(o, np.generic):
            return np.asscalar(o)
        
        return json.JSONEncoder.default(self, o)


def update(d, defaults):
    def2 = defaults.copy()
    if d is not None:
        def2.update(d)
    return def2

# Mapping Helpers

def mapping(x, y=None, color=None, shape=None, size=None):
    return {"x":x, "y":y, "color":color, "shape":shape, "size":size}


# Layout Helpers

def single():
    return {"type":"single"}

def grid(x, y, labels=True, scales="fixed", labelHeight=20):
    return {"type":"grid", "x":x, "y":y, "scales":scales, "labels":labels, "labelHeight":labelHeight}

def wrap(y, nrows=None, ncols=None, labels=True, scales="fixed", labelHeight=20):
    return {"type":"wrap", "y":y, "nrows":nrows, "ncols":ncols, "scales":scales, "labels":labels, "labelHeight":labelHeight}

def matrix(labels=True, scales="fixed", labelHeight=20):
    return {"type":"matrix", "scales":scales, "labels":labels, "labelHeight":labelHeight}


# Scales Helper

def scales(color=brewer("qual", "Accent"),
           fill=brewer("qual", "Accent"),
           shape=shapes(),
           size=None, area=None, lineType=None):
    return {"color":color, "shape":shape, "size":size, "area":area, "lineType":lineType, "fill":fill}
