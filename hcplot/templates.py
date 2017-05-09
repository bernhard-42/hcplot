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


def createGrid(containerId, width, ratio, rows, cols, rowLabels=[], colLabels=[], labelHeight=20):
    
    def sizing(width, height, rowMargin, colMargin):
        style = "width:%dpx; height:%dpx;" % (width, height)
        if colMargin != 0:
            style += " padding-left:%dpx;" % (colMargin)
        if rowMargin != 0:
            style += " padding-bottom:%dpx;" % (rowMargin)
        return style

    if len(rowLabels) > 0:   
        extraCols = len(rowLabels[0])
    else:
        extraCols = 0
    
    if len(colLabels) > 0:
        extraRows = len(colLabels[0])
    else:
        extraRows = 0

    rowStart = -extraRows
    colEnd = cols + extraCols

    w = width // cols
    h = w * ratio
    count = rows * cols
        
    html = """<table id="hc_%s" class="hcTable">\n""" % containerId
    
    for row in range(rowStart, rows):
        html += """  <tr id="hc_%s_%d" class="hcTable">\n""" % (containerId, row)

        for col in range(0, colEnd):
            
            colMargin = 50 if ((col == 0)   and (row < 0))         else 0
            rowMargin = 50 if ((col >= col) and (row == rows - 1)) else 0
            
            if row < 0 and col >= cols:
                html += """
                <th class="hcTable" style="%s"></th>""" % sizing(labelHeight, labelHeight, rowMargin, colMargin)
            elif col >= cols:
                html += """
                <th class="hcTable rowHeader" style="%s">
                    <div>%s</div>
                </th>""" % (sizing(labelHeight, h + rowMargin, rowMargin, colMargin), ("%s" % rowLabels[row][col-cols]))
            elif row < 0:
                html += """
                <th class="hcTable colHeader" style="%s">
                    <div>%s</div>
                </th>""" % (sizing(w + colMargin, labelHeight, rowMargin, colMargin), ("%s" % colLabels[col][-row -1]))
            else:
                html += """    
                <td class="hcTable">
                    <div id="hc_%s_%d-%d" style="%s"></div>
                </td>
                """ % (containerId, row, col, sizing(w + colMargin, h + rowMargin, rowMargin, colMargin))
        html += "  </tr>\n"
    html += "</table>\n"
    return html