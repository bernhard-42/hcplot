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
from .types import CSSObject, Function, Color
from .animation import _Animation
from .shadow import _Shadow
from .position import XYInteger
from .title import Title
from traitlets import Unicode, Integer, Bool, Instance


class LegendNavigation(HCBase):
    activeColor = Color(None, allow_none=True)
    animation = _Animation(None, allow_none=True)
    arrowSize = Integer(None, allow_none=True)
    enabled = Bool(None, allow_none=True)
    inactiveColor = Color(None, allow_none=True)
    style = CSSObject(None, allow_none=True)


class Legend(XYInteger):
    align = Unicode(None, allow_none=True)
    backgroundColor = Color(None, allow_none=True)
    borderColor = Color(None, allow_none=True)
    borderRadius = Integer(None, allow_none=True)
    borderWidth = Integer(None, allow_none=True)
    enabled = Bool(None, allow_none=True)
    floating = Bool(None, allow_none=True)
    itemDistance = Integer(None, allow_none=True)
    itemHiddenStyle = CSSObject(None, allow_none=True)
    itemHoverStyle = CSSObject(None, allow_none=True)
    itemMarginBottom = Integer(None, allow_none=True)
    itemMargintop = Integer(None, allow_none=True)
    itemStyle = CSSObject(None, allow_none=True)
    itemWidth = Integer(None, allow_none=True)
    labelFormat = Unicode(None, allow_none=True)
    labelFormatter = Function(None, allow_none=True)
    layout = Unicode(None, allow_none=True)
    lineHeight = Integer(None, allow_none=True)
    margin = Integer(None, allow_none=True)
    maxHeight = Integer(None, allow_none=True)
    navigation = Instance(LegendNavigation, allow_none=True)
    padding = Integer(None, allow_none=True)
    reversed_ = Bool(None, allow_none=True)
    rtl = Bool(None, allow_none=True)
    shadow = _Shadow(None, allow_none=True)          # Bool | Shadow
    squareSymbol = Bool(None, allow_none=True)
    style = CSSObject(None, allow_none=True)
    symbolHeight = Integer(None, allow_none=True)
    symbolPadding = Integer(None, allow_none=True)
    symbolRadius = Integer(None, allow_none=True)
    symbolWidth = Integer(None, allow_none=True)
    title = Instance(Title, allow_none=True)
    useHTML = Bool(None, allow_none=True)
    verticalAlign = Unicode(None, allow_none=True)
    width = Integer(None, allow_none=True)

    def __init__(self, **kwargs):
        super(__class__, self).__init__(**kwargs)         # noqa F821
