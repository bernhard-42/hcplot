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
            if value is not None:
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
                            if isinstance(value[0], HCBase):
                                result[key] = [el.toDict() for el in value]
                            else:
                                print(value)
                                result[key] = [el for el in value]
                    elif isinstance(value, dict):
                        if len(value) > 0:
                            result[key] = {k: v.toDict() for k, v in value.items()}
                    else:
                        result[key] = value
        return result

    def toJson(self, indent=None):
        return json.dumps(self.toDict(), indent=indent)
