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


class HCBase(object):

    def __init__(self, **kwargs):

        self.dict = {}
        self.setIfExists(**kwargs)

    def setIfExists(self, **kwargs):

        for k, v in kwargs.items():
            if k != "self" and v is not None:
                self.dict[k] = v

    def check(self, name, var, cls, array=False):

        if array:
            assert (var is None or (isinstance(var, (list, tuple)) and
                    len(var) > 0 and isinstance(var[0], cls))), \
                "%s must be a list of instances of class %s" % (name, cls.__name__)
        else:
            assert var is None or isinstance(var[0], cls), \
                "%s must be an instance of class %s" % (name, cls.__name__)
