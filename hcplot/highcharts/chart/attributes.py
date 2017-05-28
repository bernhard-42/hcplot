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

from ..base import HCBase


class Position(HCBase):

    def __init__(self, align=None, verticalAlign=None, x=None, y=None):

        super(__class__, self).__init__(locals())         # noqa F821


class Style(HCBase):

    def __init__(self, cursor=None, color=None, fontSize=None, textShadow=None,
                 fontWeight=None, pointerEvents=None, whiteSpace=None):

        super(__class__, self).__init__(locals())         # noqa F821


class BaseLabel(HCBase):

    def __init__(self, align=None, rotation=None, style=None, useHTML=None, x=None, y=None):

        self.check("style", style, Style)

        super(__class__, self).__init__(locals())         # noqa F821


class Label(BaseLabel):

    def __init__(self, align=None, rotation=None, style=None, useHTML=None, x=None, y=None,
                 text=None, textAlign=None, verticalAlign=None):

        self.check("style", style, Style)

        super(__class__, self).__init__(align, rotation, style, useHTML, verticalAlign, x, y)         # noqa F821

        params = {"text": text, "textAlign": textAlign, "verticalAlign": verticalAlign}
        self.setIfExists(params)


class Labels(BaseLabel):

    def __init__(self, align=None, rotation=None, style=None, useHTML=None, x=None, y=None,
                 autoRotation=None, autoRotationLimit=None, distance=None, enabled=None,
                 format_=None, formatter=None, maxStaggerLines=None, overflow=None, padding=None,
                 reserveSpace=None, staggerLines=None, step=None, zIndex=None):

        self.check("style", style, Style)

        super(__class__, self).__init__(align, rotation, style, useHTML, verticalAlign, x, y)         # noqa F821

        params = {"autoRotation": autoRotation, "autoRotationLimit": autoRotationLimit,
                  "distance": distance, "enabled": enabled, "format": format_,
                  "formatter": formatter, "maxStaggerLines": maxStaggerLines, "overflow": overflow,
                  "padding": padding, "reserveSpace": reserveSpace, "staggerLines": staggerLines,
                  "step": step, "zIndex": zIndex}
        self.setIfExists(params)


class PlotBand(HCBase):

    def __init__(self, borderColor=None, borderWidth=None, className=None, color=None, events=None,
                 from_=None, id_=None, label=None, to=None, zIndex=None):

        super(__class__, self).__init__(locals())         # noqa F821


class PlotLine(HCBase):

    def __init__(self, className=None, color=None, dashStyle=None, events=None, id_=None,
                 label=None, value=None, width=None, zIndex=None):

        super(__class__, self).__init__(locals())         # noqa F821


class BaseTitle(HCBase):

    def __init__(self, align=None, style=None, text=None, x=None, y=None):

        self.check("style", style, Style)

        super(__class__, self).__init__()         # noqa F821

        params = {"align": align, "style": style, "text": text, "x": x, "y": y}
        self.setIfExists(params)


class SubTitle(BaseTitle):

    def __init__(self, align=None, style=None, text=None, x=None, y=None,
                 useHTML=None, floating=None, verticalAlign=None, widthAdjust=None):
        self.check("style", style, Style)

        super(__class__, self).__init__(align, style, text, x, y)         # noqa F821
        params = {"useHTML": useHTML, "floating": floating, "verticalAlign": verticalAlign,
                  "widthAdjust": widthAdjust}
        self.setIfExists(params)


class Title(SubTitle):

    def __init__(self, align=None, style=None, text=None, x=None, y=None,
                 useHTML=None, floating=None, verticalAlign=None, widthAdjust=None,
                 margin=None):

        self.check("style", style, Style)

        super(__class__, self).__init__(align, style, text, x, y, useHTML, floating,     # noqa F821
                                        verticalAlign, widthAdjust)
        params = {"margin": margin}
        self.setIfExists(params)


class AxisTitle(BaseTitle):

    def __init__(self, align=None, style=None, text=None, x=None, y=None,
                 enabled=None, margin=None, offset=None, reserveSpace=None, rotation=None):
        self.check("style", style, Style)

        super(__class__, self).__init__(align, style, text, x, y)         # noqa F821
        params = {"enabled": enabled, "margin": margin, "offset": offset,
                  "reserveSpace": reserveSpace, "rotation": rotation}
        self.setIfExists(params)


class Break(HCBase):

    def __init__(self, breakSize=None, from_=None, repeat=None, to=None):

        super(__class__, self).__init__(locals())         # noqa F821


class Crosshair(HCBase):

    def __init__(self, className=None, color=None, dashStyle=None, snap=None, width=None,
                 zIndex=None):

        super(__class__, self).__init__(locals())         # noqa F821


class Credits(HCBase):

    def __init__(self, enabled=True, href=None, position=None, style=None, text=None):

        self.check("position", position, Position)
        self.check("style", style, Style)

        super(__class__, self).__init__(locals())         # noqa F821


class Events(HCBase):

    def __init__(self, addSeries=None, afterPrint=None, beforePrint=None, click=None,
                 drilldown=None, drillup=None, drillupall=None, load=None, redraw=None,
                 render=None, selection=None):

        super(__class__, self).__init__(locals())         # noqa F821


class ResetZoomButton(HCBase):

    # TODO: add theme
    def __init__(self, position=None, relativeTo=None, theme=None):

        self.check("position", position, Position)
        super(__class__, self).__init__(locals())         # noqa F821


class Chart(HCBase):

    # TODO: add options3d
    def __init__(self, alignTicks=None, animation=None, backgroundColor=None, borderColor=None,
                 borderRadius=None, borderWidth=None, className=None, colorCount=None,
                 defaultSeriesType=None, description=None, events=None, height=None,
                 ignoreHiddenSeries=None, inverted=None, margin=None, marginBottom=None,
                 marginLeft=None, marginRight=None, marginTop=None, panKey=None, panning=None,
                 pinchType=None, plotBackgroundColor=None, plotBackgroundImage=None,
                 plotBorderColor=None, plotBorderWidth=None, plotShadow=None, polar=None,
                 reflow=None, renderTo=None, resetZoomButton=None, selectionMarkerFill=None,
                 shadow=None, showAxes=None, spacing=None, spacingBottom=None, spacingLeft=None,
                 spacingRight=None, spacingTop=None, style=None, type_=None, typeDescription=None,
                 width=None, zoomType=None):

        self.check("style", style, Style)
        self.check("event", events, Events)
        self.check("resetZoomButton", resetZoomButton, ResetZoomButton)

        super(__class__, self).__init__(locals())         # noqa F821


class Data(HCBase):

    def __init__(columns=None, complete=None, csv=None, dateFormat=None, decimalPoint=None,
                 endColumn=None, endRow=None, firstRowAsNames=None, googleSpreadsheetKey=None,
                 googleSpreadsheetWorksheet=None, itemDelimiter=None, lineDelimiter="\n",
                 parseDate=None, parsed=None, rows=None, seriesMapping=None, startColumn=0,
                 startRow=0, switchRowsAndColumns=False, table=None):

        super(__class__, self).__init__(locals())         # noqa F821


class DrillUpButton(HCBase):

    def __init__(self, position=None, relativeTo=None, theme=None):

        self.check("position", position, Position)

        super(__class__, self).__init__(locals())         # noqa F821


class DrillDown(HCBase):

    def __init__(self, activeAxisLabelStyle=None, activeDataLabelStyle=None,
                 allowPointDrilldown=None, animation=None, drillUpButton=None, series=None):

        self.check("activeAxisLabelStyle", activeAxisLabelStyle, Style)
        self.check("activeDataLabelStyle", activeDataLabelStyle, Style)
        self.check("drillUpButton", drillUpButton, DrillUpButton)

        super(__class__, self).__init__(locals())         # noqa F821


class ContextButton(HCBase):
    def __init__(self, align=None, enabled=None, height=None, menuItems=None, onclick=None,
                 symbol=None, symbolFill=None, symbolSize=None, symbolStroke=None,
                 symbolStrokeWidth=None, symbolX=None, symbolY=None, text=None, theme=None,
                 verticalAlign=None, width=None, x=None, y=None):

        super(__class__, self).__init__(locals())         # noqa F821


class Buttons(HCBase):

    def __init__(self, contextButtons=None):

        self.check("contextButtons", contextButtons, ContextButton)

        super(__class__, self).__init__(locals())         # noqa F821


class ButtonOptions(HCBase):

    def __init__(self, align=None, enabled=None, height=None, symbolFill=None, symbolSize=None,
                 symbolStroke=None, symbolStrokeWidth=None, symbolX=None, symbolY=None, text=None,
                 theme=None, verticalAlign=None, width=None, y=None):

        super(__class__, self).__init__(locals())         # noqa F821


class ExportingNavigation(HCBase):

    def _init__(self, buttonOptions=None, menuItemHoverStyle=None, menuItemStyle=None,
                menuStyle=None):

        super(__class__, self).__init__(locals())         # noqa F821


class Exporting(HCBase):

    def __init__(self, allowHTML=None, buttons=None, chartOptions=None, enabled=None, error=None,
                 fallbackToExportServer=None, filename=None, formAttributes=None, libURL=None,
                 printMaxWidth=None, scale=None, sourceHeight=None, sourceWidth=None, type=None,
                 url=None, width=None):
        self.check("buttons", buttons, Buttons)


class Item(HCBase):

    def __init__(self, html=None, style=None):

        self.check("style", style, Style)

        super(__class__, self).__init__(locals())         # noqa F821


class LabelOpts(HCBase):

    def __init__(self, items=None, style=None):

        self.check("items", items, Item, True)
        self.check("style", style, Style)

        super(__class__, self).__init__(locals())         # noqa F821


class LegendNavigation(HCBase):

    def __init__(activeColor=None, animation=None, arrowSize=None, enabled=None, inactiveColor=None,
                 style=None):

        super(__class__, self).__init__(locals())         # noqa F821


class Legend(HCBase):

    def __init__(self, align=None, backgroundColor=None, borderColor=None, borderRadius=None,
                 borderWidth=None, enabled=None, floating=None, itemDistance=None,
                 itemHiddenStyle=None, itemHoverStyle=None, itemMarginBottom=None,
                 itemMarginTop=None, itemStyle=None, itemWidth=None, labelFormat=None,
                 labelFormatter=None, layout=None, lineHeight=None, margin=None, maxHeight=None,
                 navigation=None, padding=None, reversed=None, rtl=None, shadow=None,
                 squareSymbol=None, style=None, symbolHeight=None, symbolPadding=None,
                 symbolRadius=None, symbolWidth=None, title=None, useHTML=None, verticalAlign=None,
                 width=None, x=None, y=None):

        self.check("title", title, Title)
        self.check("navigation", navigation, LegendNavigation)

        super(__class__, self).__init__(locals())         # noqa F821


class NoData(HCBase):

    def __init__(self, attr=None, position=None, style=None, useHTML=None):

        self.check("position", position, Position)
        self.check("style", style, Style)

        super(__class__, self).__init__(locals())         # noqa F821


class Background(HCBase):

    def __init__(self, backgroundColor=None, borderColor=None, borderWidth=None, className=None,
                 innerRadius=None, outerRadius=None, shape=None):

        super(__class__, self).__init__(locals())         # noqa F821


class Pane(HCBase):

    def __init__(self, background=None, center=None, endAngle=None, size=None, startAngle=None):

        self.check("background", background, Background, True)

        super(__class__, self).__init__(locals())         # noqa F821


class Tooltip(HCBase):

    def __init__(self, animation=None, backgroundColor=None, borderColor=None, borderRadius=None,
                 borderWidth=None, crosshairs=None, dateTimeLabelFormats=None, enabled=None,
                 followPointer=None, followTouchMove=None, footerFormat=None, formatter=None,
                 headerFormat=None, hideDelay=None, padding=None, pointFormat=None,
                 pointFormatter=None, positioner=None, shadow=None, shape=None, shared=None,
                 snap=None, split=None, style=None, useHTML=None, valueDecimals=None,
                 valuePrefix=None, valueSuffix=None, xDateFormat=None):

        self.check("style", style, Style)

        super(__class__, self).__init__(locals())         # noqa F821


class StackLabels(HCBase):

    def __init__(self, align=None, enabled=None, format=None, formatter=None, rotation=None,
                 style=None, textAlign=None, useHTML=None, verticalAlign=None, x=None, y=None):

        self.check("style", style, Style)

        super(__class__, self).__init__(locals())         # noqa F821
