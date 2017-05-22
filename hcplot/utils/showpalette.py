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


from ..figure import Figure
from ..scales import identity
from ..config import wrap, mapping, scale
from ..geoms import Points
import pandas as pd


def showPalette(colorScale, typ=None):
    df = pd.DataFrame(colorScale.toDF(typ))
    figure = Figure(df, wrap(["palette"], ncols=3),
                    mapping("element", "size", color="color"),
                    scale(color=identity())) \
        + Points(size=8, shape="square")

    return figure
