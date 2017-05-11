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

from textwrap import dedent, indent


defaultRowMargin = 25
defaultColMargin = 50

def style(width, height, rowMargin, colMargin):
    css = "width:%dpx; height:%dpx;" % (width, height)
    css += " padding:1px 1px %dpx %dpx;" % (max(1, rowMargin), max(1, colMargin))
    return css


def indent2(text):
    return indent(dedent(text), "  ")
    

def indent4(text):
    return indent(dedent(text), "    ")


def createGrid(containerId, width, ratio, rows, cols, rowLabels=[], colLabels=[], labelHeight=20, labelAllRows=False):
    
    w = width // cols
    h = w * ratio
    
    rowHeaders = len(rowLabels[0]) if len(rowLabels) > 0 else 0
    colHeaders = len(colLabels[0]) if len(colLabels) > 0 else 0
    
    html = """<table id="hc_%s" class="hcTable">\n""" % containerId

    for row in range(rows):
        
        if labelAllRows or (colHeaders > 0 and row == 0):
            
            # print all column header hierarchies
            for c in range(colHeaders):
                html += """  <tr id="hc_%s_%d" class="hcTable">\n""" % (containerId, row)

                for col in range(cols):
                    colMargin = defaultColMargin if col == 0 and row == 0 else 0
                    html += indent4("""
                    <th class="hcTable colHeader" style="%s">
                        <div>%s</div>
                    </th>""" % (style(w + colMargin, labelHeight, 0, colMargin), colLabels[col][c]))

                # if there are row headers, print empty boxes
                for r in range(rowHeaders):
                    html += indent2("""  <th class="hcTable" style="%s">
                    </th>""" % style(labelHeight, labelHeight, 0, colMargin))

                html += "  </tr>\n"
        
        html += """  <tr id="hc_%s_%d" class="hcTable">\n""" % (containerId, row)
        for col in range(cols):
            colMargin = defaultColMargin if col == 0 else 0
            rowMargin = defaultRowMargin if row == rows - 1       else 0

            html += indent4("""    
            <td class="hcTable">
                <div id="hc_%s_%d-%d" style="%s"></div>
            </td>
            """ % (containerId, row, col, style(w + colMargin, h + rowMargin, rowMargin, 0)))
        
        # print row header hierarchies
        for r in range(rowHeaders):
            rowMargin = defaultRowMargin if row == rows - 1 else 0
            html += indent4("""
            <th class="hcTable rowHeader" style="%s">
                <div>%s</div>
            </th>""" % (style(labelHeight, h + rowMargin, rowMargin, colMargin), rowLabels[row][r]))
                
        html += "\n  </tr>\n"
    html += "</table>\n"
    return html


def createWrap(containerId, width, ratio, rows, cols, count, colLabels=[], labelHeight=20):
    w = width // cols
    h = w * ratio
    
    colHeaders = len(colLabels[0]) if len(colLabels) > 0 else 0
    
    html = """<table id="hc_%s" class="hcTable">\n""" % containerId

    i = 0
    j = 0
    for row in range(rows):
        # print all column header hierarchies
        for c in range(colHeaders):
            html += """  <tr id="hc_%s_%d" class="hcTable">\n""" % (containerId, row)
            j2 = j
            for col in range(cols):
                colMargin = defaultColMargin if col == 0 else 0
                if j2 < count:
                    html += indent4("""
                    <th class="hcTable colHeader" style="%s">
                        <div>%s</div>
                    </th>""" % (style(w + colMargin, labelHeight, 0, colMargin), colLabels[j2][c]))
                    j2 += 1
                else:
                    html += indent4("""
                    <th class="hcTable" style="%s">
                        <div></div>
                    </th>""" % (style(w + colMargin, labelHeight, 0, colMargin)))
            html += "\n  </tr>\n"
        j = j2

        html += """  <tr id="hc_%s_%d" class="hcTable">\n""" % (containerId, row)
        for col in range(cols):
            colMargin = defaultColMargin if col == 0 and row == 0 else 0
            if i < count:
                html += indent4("""    
                <td class="hcTable">
                    <div id="hc_%s_%d-%d" style="%s"></div>
                </td>
                """ % (containerId, row, col, style(w + colMargin, h + defaultRowMargin, defaultRowMargin, 0)))
            else:
                html += indent4("""    
                <td class="hcTable">
                    <div style="%s"></div>
                </td>
                """ % style(w + colMargin, h, defaultRowMargin, colMargin))
                
            i += 1

        html += "\n  </tr>\n"
    html += "</table>\n"
 
    return html
