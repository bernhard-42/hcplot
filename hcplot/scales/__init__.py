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


from .scale import Alpha, Brewer, D3, Hue, Shape, Size          # noqa F401


def defaultScales():
    return {"color": Brewer("qual", "Accent"), "shape": Shape(), "alpha": Alpha(), "size": Size()}


def identity():
    return 1


def manual(obj):
    return obj
