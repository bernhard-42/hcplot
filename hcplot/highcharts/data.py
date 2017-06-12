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
from .types import NumberOrString, Function
from traitlets import Unicode, Bool, Integer, List, Dict


class Data(HCBase):
    columns = List(List(NumberOrString(None, allow_none=True)))
    complete = Function(None, allow_none=True)
    csv = Unicode(None, allow_none=True)
    dateFormat = Unicode(None, allow_none=True)
    decimalPoInt = Unicode(None, allow_none=True)
    endColumn = Integer(None, allow_none=True)
    endRow = Integer(None, allow_none=True)
    firstRowAsNames = Bool(None, allow_none=True)
    googleSpreadsheetKey = Unicode(None, allow_none=True)
    googleSpreadsheetWorksheet = Unicode(None, allow_none=True)
    itemDelimiter = Unicode(None, allow_none=True)
    lineDelimiter = Unicode(None, allow_none=True)
    parseDate = Function(None, allow_none=True)
    parsed = Function(None, allow_none=True)
    rows = List(List(NumberOrString(None, allow_none=True)))
    seriesMapping = List(Dict(allow_none=True))
    startColumn = Integer(None, allow_none=True)
    startRow = Integer(None, allow_none=True)
    switchRowsAndColumns = Bool(None, allow_none=True)
    table = Unicode(None, allow_none=True)
