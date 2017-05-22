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


from .figure import Figure 									          # noqa F401
from .config  import mapping, single, matrix, grid ,wrap, scale       # noqa F401

import os
from IPython.display import HTML, Javascript, display


def loadLibraries():
    folder = os.path.dirname(__file__)

    with open(os.path.join(folder, "./css", "styles.css"), "r") as fd:
        css = fd.read()
    display(HTML("<style>%s</style>" % css))

    with open(os.path.join(folder, "./js", "load.js"), "r") as fd:
        js = fd.read()
    display(Javascript(js))


def loadBoost(commit="593c569"):
    folder = os.path.dirname(__file__)

    with open(os.path.join(folder, "./js", "load-boost.js"), "r") as fd:
        js = fd.read()

    display(Javascript(js % commit))


msg = """
- Highsoft software products (www.highcharts.com) are not free for commercial and Governmental use.
  (see https://shop.highsoft.com/faq#Non-Commercial-0 for conditions for Non-commercial use).
- This product includes color specifications and designs developed by Cynthia Brewer
  http://colorbrewer.org
- D3 category colors and the interpolateRGB algorithm have been taken over from https://d3js.org/,
  Copyright 2010-2017 Mike Bostock
"""
print(msg)
