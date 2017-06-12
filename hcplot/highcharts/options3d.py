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

from .base import HCBase
from .color import Color
from .types import BoolOrString
from traitlets import Integer, Instance, Bool, Unicode


class FrameOptions(HCBase):
    color = Color(None, allow_none=True)
    size = Integer(None, allow_none=True)


class FrameOptions2(FrameOptions):
    visible = BoolOrString(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821


class Frame(HCBase):
    back = Instance(FrameOptions2, allow_none=True)
    bottom = Instance(FrameOptions2, allow_none=True)
    side = Instance(FrameOptions, allow_none=True)
    top = Instance(FrameOptions, allow_none=True)


class Options3d(HCBase):
    alpha = Integer(None, allow_none=True)
    axisLabelPosition = Unicode(None, allow_none=True)
    beta = Integer(None, allow_none=True)
    depth = Integer(None, allow_none=True)
    enabled = Bool(None, allow_none=True)
    fitToPlot = Bool(None, allow_none=True)
    frame = Instance(Frame, allow_none=True)
    viewDistance = Integer(None, allow_none=True)
