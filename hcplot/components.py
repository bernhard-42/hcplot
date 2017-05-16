
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

class Components(object):

    def figure(self, zoomType="xy", title=None, exporting=True, legend=True):
        self.figure = {
            "chart":     { 
                "zoomType": zoomType,
                "spacingBottom": 5,
                "spacingTop": 5,
                "spacingLeft": 5,
                "spacingRight": 5
            },
            "credits" : {
                "position": {"y": -5}
            },
            "exporting": { "enabled": exporting },
            "title":     { "text": title },
            "legend":    { "enabled": legend },
            "series":    []
        }
        return self


    def get(self):
        return self.figure


    def updateFigure(self, **options):
        self.figure.update(options)
        return self

    def updateChart(self, **options):
        self.figure["chart"].update(options)
        return self

    def _cleanOptions(self, options):
        
        def setAttr(key, attr, options):
            if key in options.keys():
                options[key] = { attr: options[key] }

        def setEnabled(key, options):
            setAttr(key, "enabled", options)

        def setText(key, options):
            setAttr(key, "text", options)

        setText("title", options)
        setEnabled("legend", options)
        setEnabled("labels", options)


    def _addAxis(self, ax, options):
        self._cleanOptions(options)
        self.figure[ax] = options


    def addXAxis(self, *args, **options):
        self._addAxis("xAxis", options)
        return self


    def addYAxis(self, *args, **options):
        self._addAxis("yAxis", options)
        return self


    def _updateAxis(self, ax, options):
        self._cleanOptions(options)
        self.figure[ax].update(options)

    
    def updateXAxis(self, **options):
        self._updateAxis("xAxis", options)
        return self

    
    def updateYAxis(self, **options):
        self._updateAxis("yAxis", options)
        return self


    def addSeries(self, name, data, options):
        series = { "name": name, "data": data }
        series.update(options)
        self.figure["series"].append(series)
        return self


    @classmethod
    def point(cls, names, values):
        result = {}
        for name, value in zip(names, values):
            if name in ["x", "y", "color"]:
                result[name] = value
            elif name == "shape":
                if result.get("marker") is None:
                    result["marker"] = {}
                result["marker"]["symbol"] = value
            elif name == "size":
                if result.get("marker") is None:
                    result["marker"] = {}
                result["marker"]["radius"] = value
        return result