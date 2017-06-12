
class HCBase(object):
    def __init__(self, **kwargs):
        self.dict = {}
        self.setIfExists(**kwargs)

    def setIfExists(**kwargs):
        for k,v in kwargs.items():
            if if k != "self" and v is not None:
                self.dict[k] = v

    def check(self, name, var, cls, array=False):
        if array:
            assert var is None or (isinstance(var, (list, tuple)) and len(var) > 0 and isinstance(var[0], cls)),
                "%s must be a list of instances of class %s" % (name, cls.__name__)
        else:
            assert var is None or isinstance(var[0], cls),
                "%s must be an instance of class %s" % (name, cls.__name__)


class Position(HCBase):

    def __init__(self, align=None, verticalAlign=None, x=None, y=None):
        
        super(__class__, self).__init__(locals())


class Style(HCBase):

    def __init__(self, cursor=None, color=None, fontSize=None, textShadow=None, 
                 fontWeight=None, pointerEvents=None, whiteSpace=None):
        
        super(__class__, self).__init__(locals())


class BaseLabel(HCBase):

    def __init__(self, align=None, rotation=None, style=None, useHTML=None, x=None, y=None):
        
        self.check("style", style, Style)

        super(__class__, self).__init__(locals())


class Label(BaseLabel):

    def __init__(self, align=None, rotation=None, style=None, useHTML=None, x=None, y=None, 
                 text=None, textAlign=None, verticalAlign=None):
        
        self.check("style", style, Style)

        super(__class__, self).__init__(align, rotation, style, useHTML, verticalAlign, x, y)
        
        params = {"text": text, "textAlign": textAlign, "verticalAlign": verticalAlign}
        self.setIfExists(params)


class Labels(BaseLabel):

    def __init__(self, align=None, rotation=None, style=None, useHTML=None, x=None, y=None, 
                 autoRotation=None, autoRotationLimit=None, distance=None, enabled=None, 
                 format_=None, formatter=None, maxStaggerLines=None, overflow=None, padding=None, 
                 reserveSpace=None, staggerLines=None, step=None, zIndex=None):
        
        self.check("style", style, Style)

        super(__class__, self).__init__(align, rotation, style, useHTML, verticalAlign, x, y)
        
        params = {"autoRotation": autoRotation, "autoRotationLimit": autoRotationLimit, 
                  "distance": distance, "enabled": enabled, "format": format_, "formatter": formatter, 
                  "maxStaggerLines": maxStaggerLines, "overflow": overflow, "padding": padding, 
                  "reserveSpace": reserveSpace, "staggerLines": staggerLines,"step": step, "zIndex": zIndex}
        self.setIfExists(params)


class PlotBand(HCBase):

    def __init__(self, borderColor=None, borderWidth=None, className=None, color=None, events=None, 
                 from_=None, id_=None, label=None, to=None, zIndex=None):
        
        super(__class__, self).__init__(locals())


class PlotLine(HCBase):

    def __init__(self, className=None, color=None, dashStyle=None, events=None, id_=None, label=None, 
                 value=None, width=None, zIndex=None):
        
        super(__class__, self).__init__(locals())


class BaseTitle(HCBase):

    def __init__(self, align=None, style=None, text=None, x=None, y=None):
        
        self.check("style", style, Style)
    
        super(__class__, self).__init__()
        
        params = {"align"=align, "style"=style, "text"=text, "x"=x, "y"=y}
        self.setIfExists(params)


class SubTitle(BaseTitle):

    def __init__(self, align=None, style=None, text=None, x=None, y=None, 
                 useHTML=None, floating=None, verticalAlign=None, widthAdjust=None):
        self.check("style", style, Style)
     
        super(__class__, self).__init__(align, style, text, x, y)
        params = {"useHTML": useHTML, "floating": floating, "verticalAlign": verticalAlign, 
                  "widthAdjust": widthAdjust}
        self.setIfExists(params)


class Title(SubTitle):

    def __init__(self, align=None, style=None, text=None, x=None, y=None, 
                 useHTML=None, floating=None, verticalAlign=None, widthAdjust=None, 
                 margin=None):
        
        self.check("style", style, Style)
    
        super(__class__, self).__init__(align, style, text, x, y, useHTML, floating, verticalAlign, 
                                        widthAdjust)
        params = {"margin": margin}
        self.setIfExists(params)


class AxisTitle(BaseTitle):

    def __init__(self, align=None, style=None, text=None, x=None, y=None, 
                 enabled=None, margin=None, offset=None, reserveSpace=None, rotation=None):
        self.check("style", style, Style)
        
        super(__class__, self).__init__(align, style, text, x, y)
        params = {"enabled": enabled, "margin": margin, "offset": offset, "reserveSpace": reserveSpace, 
                  "rotation": rotation}
        self.setIfExists(params)


class Break(HCBase):

    def __init__(self, breakSize=None, from_=None, repeat=None, to=None):
    
        super(__class__, self).__init__(locals())


class Crosshair(HCBase):

    def __init__(self, className=None, color=None, dashStyle=None, snap=None, width=None, zIndex=None):
    
        super(__class__, self).__init__(locals())


class Credits(HCBase):

    def __init__(self, enabled=True, href=None, position=None, style=None, text=None):
        
        self.check("position", position, Position)
        self.check("style", style, Style)
    
        super(__class__, self).__init__(locals())


class Events(HCBase):

    def __init__(self addSeries=None, afterPrint=None, beforePrint=None, click=None, drilldown=None, drillup=None,
                 drillupall=None, load=None, redraw=None, render=None, selection=None):

        super(__class__, self).__init__(locls())


class Chart(HCBase):

    def __init__(self, alignTicks=None, animation=None, backgroundColor=None, borderColor=None,
                 borderRadius=None, borderWidth=None, className=None, colorCount=None, 
                 defaultSeriesType=None, description=None, events=None, height=None, 
                 ignoreHiddenSeries=None, inverted=None, margin=None, marginBottom=None, marginLeft=None, 
                 marginRight=None, marginTop=None, panKey=None, panning=None, pinchType=None, 
                 plotBackgroundColor=None, plotBackgroundImage=None, plotBorderColor=None, 
                 plotBorderWidth=None, plotShadow=None, polar=None, reflow=None, renderTo=None, 
                 selectionMarkerFill=None, shadow=None, showAxes=None, spacing=None, spacingBottom=None, 
                 spacingLeft=None, spacingRight=None, spacingTop=None, style=None, type_=None, 
                 typeDescription=None, width=None, zoomType=None):
        
        self.check("style", style, Style)
        self.check("event", event, Event)
    
        super(__class__, self).__init__(locals())


class Data(HCBase):

    def __init__(columns=None, complete=None, csv=None, dateFormat=None, decimalPoint=None, endColumn=None, 
                 endRow=None, firstRowAsNames=None, googleSpreadsheetKey=None, googleSpreadsheetWorksheet=None, 
                 itemDelimiter=None, lineDelimiter= "\n", parseDate=None, parsed=None, rows=None, 
                 seriesMapping= None, startColumn= 0, startRow= 0, switchRowsAndColumns= False, table=None) 
    
        super(__class__, self).__init__(locals())


class DrillButton(HCBase):
    
    def __init__(self, position=None, relativeTo=None, theme=None)
        
        self.check("position", position, Position)

        super(__class__, self).__init__(locals())


class DrillDown(HCBase):
    
    def __init__(self, activeAxisLabelStyle=None, activeDataLabelStyle=None, allowPointDrilldown=None, 
                 animation=None, drillUpButton=None, series=None):
    
        self.check("activeAxisLabelStyle", activeAxisLabelStyle, Style)
        self.check("activeDataLabelStyle", activeDataLabelStyle, Style)
        self.check("drillUpButton", drillUpButton, DrillUpButton)

        super(__class__, self).__init__(locals())


class ContextButton(HCBase):
    def __init__(self, align=None, enabled=None, height=None, menuItems=None, onclick=None, symbol=None, 
                 symbolFill=None, symbolSize=None, symbolStroke=None, symbolStrokeWidth=None, symbolX=None, 
                 symbolY=None, text=None, theme=None, verticalAlign=None, width=None, x=None, y=None):

        super(__class__, self).__init__(locals())


class Buttons(HCBase):

    def __init__(self, contextButtons=None):

        self.check("contextButtons", contextButtons, ContextButtons)

        super(__class__, self).__init__(locals())

class ButtonOptions(HCBase):

    def __init__(self, align=None, enabled=None, height=None, symbolFill=None, symbolSize=None, 
                 symbolStroke=None, symbolStrokeWidth=None, symbolX=None, symbolY=None, text=None, 
                 theme=None, verticalAlign=None, width=None, y=None):

        super(__class__, self).__init__(locals())


class ExportingNavigation(HCBase):
    
    def _init__(self, buttonOptions=None, menuItemHoverStyle=None, menuItemStyle=None, menuStyle=None):

        super(__class__, self).__init__(locals())


class Exporting(HCBase):

    def __init__(self, allowHTML=None, buttons=None, chartOptions=None, enabled=None, error=None, 
                 fallbackToExportServer=None, filename=None, formAttributes=None, libURL=None, 
                 printMaxWidth=None, scale=None, sourceHeight=None, sourceWidth=None, type=None, 
                 url=None, width=None):
        self.check("buttons", buttons, Buttons)


class Item(HCBase):

    def __init__(html=None, style=None):
        
        self.check("style", style, Style)
    
        super(__class__, self).__init__(locals())


class LabelOpts(HCBase):

    def __init__(items=None, style=None):
        
        self.check("items", items, Item, True)
        self.check("style", style, Style)
        
        super(__class__, self).__init__(locals())


class LegendNavigation(HCBase):
    
    def __init__(activeColor=None, animation=None, arrowSize=None, enabled=None, inactiveColor=None, style=None):
    
        super(__class__, self).__init__(locals())


class Legend(HCBase):
    
    def __init__(self, align=None, backgroundColor=None, borderColor=None, borderRadius=None, borderWidth=None, 
                 enabled=None, floating=None, itemDistance=None, itemHiddenStyle=None, itemHoverStyle=None, 
                 itemMarginBottom=None, itemMarginTop=None, itemStyle=None, itemWidth=None, labelFormat=None, 
                 labelFormatter=None, layout=None, lineHeight=None, margin=None, maxHeight=None, navigation=None, 
                 padding=None, reversed=None, rtl=None, shadow=None, squareSymbol=None, style=None, symbolHeight=None, 
                 symbolPadding=None, symbolRadius=None, symbolWidth=None, title=None, useHTML=None, verticalAlign=None, 
                 width=None, x=None, y=None)
        
        self.check("title", title, Title)
        self.check("navigation", navigation, LegendNavigation)
    
        super(__class__, self).__init__(locals())


class NoData(HCBase):
    
    def __init__(self, attr=None, position=None, style=None, useHTML=None):

        self.check("position", position, Position)
        self.check("style", style, Style)

        super(__class__, self).__init__(locals())

class Background(HCBase):
    
    def __init__(self, backgroundColor=None, borderColor=None, borderWidth=None, className=None, 
                 innerRadius=None, outerRadius=None, shape=None):

        super(__class__, self).__init__(locals())


class Pane(HCBase):

    def __init__(self, background=None, center=None, endAngle=None, size=None, startAngle=None):

        self.check("background", background, Background, True)

        super(__class__, self).__init__(locals())


class Tooltip(HCBase)
    
    def __init__(self, animation=None, backgroundColor=None, borderColor=None, borderRadius=None, borderWidth=None, 
                 crosshairs=None, dateTimeLabelFormats=None, enabled=None, followPointer=None, followTouchMove=None, 
                 footerFormat=None, formatter=None, headerFormat=None, hideDelay=None, padding=None, pointFormat=None, 
                 pointFormatter=None, positioner=None, shadow=None, shape=None, shared=None, snap=None, split=None, 
                 style=None, useHTML=None, valueDecimals=None, valuePrefix=None, valueSuffix=None, xDateFormat=None)

        self.check("style", style, Style)
    
        super(__class__, self).__init__(locals())


class StackLabels(HCBase):
    
    def __init__(self, align=None, enabled=None, format=None, formatter=None, rotation=None, style=None, 
                 textAlign=None, useHTML=None, verticalAlign=None, x=None, y=None):
        
        self.check("style", style, Style)
    
        super(__class__, self).__init__(locals())


class Axis(HCBase):

    def __init__(self, allowDecimals=None, alternateGridColor=None, breaks=None, categories=None, ceiling=None, 
                 className=None, crosshair=None, dateTimeLabelFormats=None, description=None, endOnTick=None, 
                 events=None, floor=None, gridLineColor=None, gridLineDashStyle=None, gridLineWidth=None, id_=None, 
                 labels=None, lineColor=None, lineWidth=None, linkedTo=None, max_=None, maxPadding=None, maxZoom=None, 
                 min_=None, minPadding=None, minRange=None, minTickInterval=None, minorGridLineColor=None, 
                 minorGridLineDashStyle=None, minorGridLineWidth=None, minorTickColor=None, minorTickInterval=None, 
                 minorTickLength=None, minorTickPosition=None, minorTickWidth=None, offset=None, opposite=None, 
                 plotBands=None, plotLines=None, reversed_=None, showEmpty=None, showFirstLabel=None, showLastLabel=None, 
                 softMax=None, softMin=None, startOfWeek=None, startOnTick=None, tickAmount=None, tickColor=None, 
                 tickInterval=None, tickLength=None, tickPixelInterval=None, tickPosition=None, tickPositioner=None, 
                 tickPositions=None, tickWidth=None, tickmarkPlacement=None, title=None, type_=None, uniqueNames=None, 
                 units=None, visible=None):

        self.check("label", label, Label)
        self.check("plotLines", plotLines, PlotLine, True)
        self.check("plotBands", plotBands, PlotBands, True)
        self.check("title", title, title)
        self.check("crosshair", crosshair, crosshair)
        super(__class__, self).__init__(locals())


class XAxis(Axis):

    def __init__(self, allowDecimals=None, alternateGridColor=None, breaks=None, categories=None, ceiling=None, 
                 className=None, crosshair=None, dateTimeLabelFormats=None, description=None, endOnTick=None, 
                 events=None, floor=None, gridLineColor=None, gridLineDashStyle=None, gridLineWidth=None, id_=None, 
                 labels=None, lineColor=None, lineWidth=None, linkedTo=None, max_=None, maxPadding=None, maxZoom=None, 
                 min_=None, minPadding=None, minRange=None, minTickInterval=None, minorGridLineColor=None, 
                 minorGridLineDashStyle=None, minorGridLineWidth=None, minorTickColor=None, minorTickInterval=None, 
                 minorTickLength=None, minorTickPosition=None, minorTickWidth=None, offset=None, opposite=None, 
                 plotBands=None, plotLines=None, reversed_=None, showEmpty=None, showFirstLabel=None, showLastLabel=None, 
                 softMax=None, softMin=None, startOfWeek=None, startOnTick=None, tickAmount=None, tickColor=None, 
                 tickInterval=None, tickLength=None, tickPixelInterval=None, tickPosition=None, tickPositioner=None, 
                 tickPositions=None, tickWidth=None, tickmarkPlacement=None, title=None, type_=None, uniqueNames=None, 
                 units=None, visible=None):

        self.check("breaks", breaks, Break, True)
 
        super(__class__, self).__init__(allowDecimals, alternateGridColor, categories, ceiling,
                                        className, crosshair, dateTimeLabelFormats, description, endOnTick, 
                                        events, floor, gridLineColor, gridLineDashStyle, gridLineWidth, id_, 
                                        labels, lineColor, lineWidth, linkedTo, max_, maxPadding, maxZoom, 
                                        min_, minPadding, minRange, minTickInterval, minorGridLineColor, 
                                        minorGridLineDashStyle, minorGridLineWidth, minorTickColor, 
                                        minorTickInterval, minorTickLength, minorTickPosition, minorTickWidth, 
                                        offset, opposite, plotBands, plotLines, reversed_, showEmpty, 
                                        showFirstLabel, showLastLabel, softMax, softMin, startOfWeek, 
                                        startOnTick, tickAmount, tickColor, tickInterval, tickLength, 
                                        tickPixelInterval, tickPosition, tickPositioner, tickPositions, 
                                        tickWidth, tickmarkPlacement, title, type_, uniqueNames, units, visible)
        params = {"breaks": breaks}
        self.setIfExists(params)


class YAxis(Axis):

    def __init__(self, allowDecimals=None, alternateGridColor=None, breaks=None, categories=None, ceiling=None, 
                 className=None, crosshair=None, dateTimeLabelFormats=None, description=None, endOnTick=None, 
                 events=None, floor=None, gridLineColor=None, gridLineDashStyle=None, gridLineWidth=None, id_=None, 
                 labels=None, lineColor=None, lineWidth=None, linkedTo=None, max_=None, maxPadding=None, maxZoom=None, 
                 min_=None, minPadding=None, minRange=None, minTickInterval=None, minorGridLineColor=None, 
                 minorGridLineDashStyle=None, minorGridLineWidth=None, minorTickColor=None, minorTickInterval=None, 
                 minorTickLength=None, minorTickPosition=None, minorTickWidth=None, offset=None, opposite=None, 
                 plotBands=None, plotLines=None, reversed_=None, showEmpty=None, showFirstLabel=None, showLastLabel=None, 
                 softMax=None, softMin=None, startOfWeek=None, startOnTick=None, tickAmount=None, tickColor=None, 
                 tickInterval=None, tickLength=None, tickPixelInterval=None, tickPosition=None, tickPositioner=None, 
                 tickPositions=None, tickWidth=None, tickmarkPlacement=None, title=None, type_=None, uniqueNames=None, 
                 units=None, visible=None):

        self.check("stackLabels", stackLabels, StackLabels)
        self.check("breaks", breaks, Break, True)

        super(__class__, self).__init__(allowDecimals, alternateGridColor, categories, ceiling,
                                        className, crosshair, dateTimeLabelFormats, description, endOnTick, 
                                        events, floor, gridLineColor, gridLineDashStyle, gridLineWidth, id_, 
                                        labels, lineColor, lineWidth, linkedTo, max_, maxPadding, maxZoom, 
                                        min_, minPadding, minRange, minTickInterval, minorGridLineColor, 
                                        minorGridLineDashStyle, minorGridLineWidth, minorTickColor, 
                                        minorTickInterval, minorTickLength, minorTickPosition, minorTickWidth, 
                                        offset, opposite, plotBands, plotLines, reversed_, showEmpty, 
                                        showFirstLabel, showLastLabel, softMax, softMin, startOfWeek, 
                                        startOnTick, tickAmount, tickColor, tickInterval, tickLength, 
                                        tickPixelInterval, tickPosition, tickPositioner, tickPositions, 
                                        tickWidth, tickmarkPlacement, title, type_, uniqueNames, units, visible)

        params = {"angle": angle, "breaks": breaks, "gridLineInterpolation": gridLineInterpolation, "gridZIndex": gridZIndex, 
                  "maxColor": maxColor, "minColor": minColor, "reversedStacks": reversedStacks, 
                  "stackLabels": stackLabels, "stops": stops}
        self.setIfExists(params)


class ZAxis(Axis):
  
    def __init__(self, allowDecimals=None, alternateGridColor=None, categories=None, ceiling=None, 
                 className=None, crosshair=None, dateTimeLabelFormats=None, description=None, endOnTick=None, 
                 events=None, floor=None, gridLineColor=None, gridLineDashStyle=None, gridLineWidth=None, id_=None, 
                 labels=None, lineColor=None, lineWidth=None, linkedTo=None, max_=None, maxPadding=None, maxZoom=None, 
                 min_=None, minPadding=None, minRange=None, minTickInterval=None, minorGridLineColor=None, 
                 minorGridLineDashStyle=None, minorGridLineWidth=None, minorTickColor=None, minorTickInterval=None, 
                 minorTickLength=None, minorTickPosition=None, minorTickWidth=None, offset=None, opposite=None, 
                 plotBands=None, plotLines=None, reversed_=None, showEmpty=None, showFirstLabel=None, showLastLabel=None, 
                 softMax=None, softMin=None, startOfWeek=None, startOnTick=None, tickAmount=None, tickColor=None, 
                 tickInterval=None, tickLength=None, tickPixelInterval=None, tickPosition=None, tickPositioner=None, 
                 tickPositions=None, tickWidth=None, tickmarkPlacement=None, title=None, type_=None, uniqueNames=None, 
                 units=None, visible=None):

        super(__class__, self).__init__(allowDecimals, alternateGridColor, categories, ceiling,
                                        className, crosshair, dateTimeLabelFormats, description, endOnTick, 
                                        events, floor, gridLineColor, gridLineDashStyle, gridLineWidth, id_, 
                                        labels, lineColor, lineWidth, linkedTo, max_, maxPadding, maxZoom, 
                                        min_, minPadding, minRange, minTickInterval, minorGridLineColor, 
                                        minorGridLineDashStyle, minorGridLineWidth, minorTickColor, 
                                        minorTickInterval, minorTickLength, minorTickPosition, minorTickWidth, 
                                        offset, opposite, plotBands, plotLines, reversed_, showEmpty, 
                                        showFirstLabel, showLastLabel, softMax, softMin, startOfWeek, 
                                        startOnTick, tickAmount, tickColor, tickInterval, tickLength, 
                                        tickPixelInterval, tickPosition, tickPositioner, tickPositions, 
                                        tickWidth, tickmarkPlacement, title, type_, uniqueNames, units, visible)

class Figure(HCBase):
    def __init__(self, chart=None, colors=None, credits=None, data=None, drilldown=None, exporting=None, 
                labels=None, legend=None, loading=None, navigation=None, noData=None, pane=None, 
                plotOptions=None, responsive=None, series=None, subtitle=None, title=None, tooltip=None, 
                xAxis=None, yAxis=None, zAxis=None):
        
        self.check("chart", chart, Chart)
        self.check("colors", colors, list)
        self.check("credits", credits, Credits)
        self.check("data", data, Data)
        self.check("drilldown", drilldown, Drilldown)
        self.check("exporting", exporting, Exporting)
        self.check("labels", labels, Labels)
        self.check("legend", legend, Legend)
        self.check("navigation", navigation, ExportingNavigation)
        self.check("noData", noData, NoData)
        self.check("pane", pane, Pane)
#        self.check("plotOptions", plotOptions, PlotOptions)
        self.check("responsive", responsive, Responsive)
        self.check("series", series, Series)
        self.check("subtitle", subtitle, Subtitle)
        self.check("title", title, Title)
        self.check("tooltip", tooltip, Tooltip)
        self.check("xAxis", xAxis, XAxis)
        self.check("yAxis", yAxis, YAxis)
        self.check("zAxis", zAxis, ZAxis)




















