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

# Mapping Helpers

def mapping(x, y=None):
    return {"x":x, "y":y}

# Layout Helpers

def single():
    return {"type":"single"}

def grid(x, y, labels=True, labelHeight=20):
    return {"type":"grid", "x":x, "y":y, "labels":labels, "labelHeight":labelHeight}

def wrap(y, nrows=None, ncols=None, labels=True, labelHeight=20):
    return {"type":"wrap", "y":y, "nrows":nrows, "ncols":ncols, "labels":labels, "labelHeight":labelHeight}

def matrix(labels=True, labelHeight=20):
    return {"type":"matrix", "labels":labels, "labelHeight":labelHeight}

