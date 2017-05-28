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

from ..base import HCBase
from .attributes import Chart, Credits, Data, Drilldown, Exporting, Labels, Legend, Tooltip
from .attributes import ExportingNavigation, NoData, Pane, Responsive, Series, Subtitle, Title
from .axis import XAxis, YAxis, ZAxis


class Figure(HCBase):
    def __init__(self, chart=None, colors=None, credits=None, data=None, drilldown=None,
                 exporting=None, labels=None, legend=None, loading=None, navigation=None,
                 noData=None, pane=None, plotOptions=None, responsive=None, series=None,
                 subtitle=None, title=None, tooltip=None, xAxis=None, yAxis=None, zAxis=None):

        self.check("chart", chart, Chart)
        self.check("colors", colors, list)
        self.check("credits", credits, Credits)
        self.check("data", data, Data)
        self.check("drilldown", drilldown, Drilldown)
        self.check("exporting", exporting, Exporting)
        self.check("labels", labels, Labels)
        self.check("legend", legend, Legend)
        self.check("navigation", navigation, ExportingNavigation)
        self.check("noData", noData, NoData)
        self.check("pane", pane, Pane)
#        self.check("plotOptions", plotOptions, PlotOptions)
        self.check("responsive", responsive, Responsive)
        self.check("series", series, Series)
        self.check("subtitle", subtitle, Subtitle)
        self.check("title", title, Title)
        self.check("tooltip", tooltip, Tooltip)
        self.check("xAxis", xAxis, XAxis)
        self.check("yAxis", yAxis, YAxis)
        self.check("zAxis", zAxis, ZAxis)
