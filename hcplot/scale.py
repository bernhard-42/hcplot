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

from .color import ColorBrewer, D3Colors
from .shape import Shape

def brewer(typ, palette):
    return lambda size: getattr(ColorBrewer, typ)(palette, size)

def d3(typ):
    return getattr(D3Colors, typ)

def shapes():
    return Shape.get


# class Scale(object):
    
#     def __init__(self):
#         pass


# class Color(Scale):

#     @classmethod
#     def brewer(self, typ, palette):
#         return lambda size: getattr(ColorBrewer, typ)(palette, size)

#     @classmethod
#     def d3(self, typ):
#         return getattr(D3Colors, typ)