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

from traitlets import HasTraits
import json


class HCBase(HasTraits):

    def toDict(self):
        result = {}
        for key, cls in self.class_traits().items():
            value = getattr(self, key)
            if value is None:
                if key in ["text"]:
                    return {key: None}
            else:
                if key[-1] == "_":
                    key = key[:-1]
                key = key.replace("_", "")

                if isinstance(value, HCBase):
                    result[key] = value.toDict()
                elif hasattr(cls, "conv"):
                    result[key] = cls.conv(value)
                else:
                    if isinstance(value, (tuple, list)):
                        if len(value) > 0:
                            result[key] = []
                            for el in value:
                                if isinstance(el, HCBase):
                                    if hasattr(el, "conv"):
                                        result[key].append(el.conv(el.toDict()))
                                    else:
                                        result[key].append(el.toDict())
                                else:
                                    result[key].append(el)
                    elif isinstance(value, dict):
                        if len(value) > 0:
                            result[key] = {k: v.toDict() for k, v in value.items()}
                    else:
                        result[key] = value
        return result

    def toJson(self, indent=None):
        return json.dumps(self.toDict(), indent=indent)

    @staticmethod
    def conv(value):
        return value
