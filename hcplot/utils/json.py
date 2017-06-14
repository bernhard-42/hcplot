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

import json
import datetime
import pandas as pd
import numpy as np


class ScipyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, pd.tslib.Timestamp):
            o = o.to_pydatetime()

        if isinstance(o, datetime.datetime):
            return int(o.timestamp() * 1000)

        if isinstance(o, np.generic):
            return np.asscalar(o)

        return json.JSONEncoder.default(self, o)
