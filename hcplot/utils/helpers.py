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


import numpy as np
import pandas as pd


def update(d, defaults):
    def2 = defaults.copy()
    if d is not None:
        def2.update(d)
    return def2


def reshape(s):
    if isinstance(s, (list, tuple)):
        return np.array(s).reshape(-1, 1)
    elif isinstance(s, np.ndarray):
        return s.reshape(-1, 1)
    elif isinstance(s, pd.core.series.Series):
        return s.values.reshape(-1, 1)
