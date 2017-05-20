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

import math


class Shape(object):
    shapes = ["circle", "triangle", "triangle-down", "diamond", "square"]

    #
    # Get discrete results
    #

    @classmethod
    def _get(cls, size):
        if size < len(Shape.shapes):
            return Shape.shapes[:size]
        else:
            factor = math.ceil(size / (len(Shape.shapes) - 3))
            return (Shape.shapes * factor)[:size]

    #
    # Accessors
    #

    @classmethod
    def shape(cls, size):
        return cls._get(size)


#
# Quick Accessor
#

def shape(size):
    return Shape.shape(size)
