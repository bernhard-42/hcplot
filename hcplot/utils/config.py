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


class Config(object):
    def __init__(self, param, config, **kwargs):
        self.param = param
        self.config = self._dropNone(config)
        self.config.update(kwargs)

    def _dropNone(self, d):
        return {k:v for k,v in d.items() if v is not None}


# Mapping Helper

def mapping(x, y=None, color=None, shape=None, size=None):
    return Config("mapping", locals())


# Layout Helpers

def single(labels=True):
    return Config("layout", locals(), type="single")

def matrix(labels=True, scales="fixed", labelHeight=20):
    return Config("layout", locals(), type="matrix")

def grid(x, y, labels=True, scales="fixed", labelHeight=20):
    return Config("layout", locals(), type="grid")

def wrap(y, nrows=None, ncols=None, labels=True, scales="fixed", labelHeight=20):
    return Config("layout", locals(), type="wrap")


# Scales Helper

def scales(color=None, shape=None, size=None, area=None, lineType=None):
    return Config("scales", locals())


# Scales Helper

def scales(color=None, shape=None, size=None, area=None, lineType=None):
    return Config("scales", locals())
