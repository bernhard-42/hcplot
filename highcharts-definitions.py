class Position(object):
	def __init__(self, align, verticalAlign, x, y):
		self.json = {
			"align": align,
			"verticalAlign": verticalAlign,
			"x": x,
			"y": y
		}

class Style(object):
	def __init__(self, cursor=None, color=None, fontSize=None, textShadow=None, fontWeight=None, pointerEvents=None, whiteSpace=None):
		self.json = {}
		if cursor is not None:
			self.json[cursor] = cursor
		if color is not None:
			self.json[color] = color
		if fontSize is not None:
			self.json[fontSize] = fontSize
		if textShadow is not None:
			self.json[textShadow] = textShadow
		if fontWeight is not None:
			self.json[fontWeight] = fontWeight
		if pointerEvents is not None:
			self.json[pointerEvents] = pointerEvents
		if whiteSpace is not None:
			self.json[whiteSpace] = whiteSpace

class BaseLabel(object):
	def __init__(self, align, rotation, style, useHTML, x, y):
		self.json = {
			"align": align,
			"rotation": rotation,
			"style": style,
			"useHTML": useHTML,
			"x": x,
			"y": y
		}

class Label(object):
	def __init__(self, align, rotation, style, text, textAlign, useHTML, verticalAlign, x, y):
		super(__class__, self).__init__(align, rotation, style, useHTML, verticalAlign, x, y)
		options = {"text": text, 
		           "textAlign": textAlign, 
		           "verticalAlign": verticalAlign}
		self.json.update(options)

class Labels(BaseLabel):
	def __init__(self, align, autoRotation, autoRotationLimit, distance, enabled, format, formatter, maxStaggerLines,
	             overflow, padding, reserveSpace, rotation, staggerLines, step, style, useHTML, x, y, zIndex):
		super(__class__, self).__init__(align, rotation, style, useHTML, verticalAlign, x, y)
		options={"autoRotation": autoRotation, 
		         "autoRotationLimit": autoRotationLimit, 
		         "distance": distance, 
		         "enabled": enabled, 
		         "format": format, 
		         "formatter": formatter, 
		         "maxStaggerLines": maxStaggerLines, 
		         "overflow": overflow, 
		         "padding": padding, 
		         "reserveSpace": reserveSpace, 
		         "staggerLines": staggerLines, 
		         "step": step, 
		         "zIndex": zIndex, }
		 self.json.update(options)

class PlotBand(object): 
	def __init__(self, borderColor, borderWidth, className, color, events, from_, id, label, to, zIndex):
	self.json = {
		"borderColor": borderColor,
		"borderWidth": borderWidth,
		"className":NclassName,
		"color": color,
		"events": events,
		"from": from_,
		"id": id,
		"label": label,
		"to": to,
		"zIndex": zIndex
	}

class PlotLine(object): 
	def __init__(self, className, color, dashStyle, events, id, label, value, width, zIndex):
	self.json = {
		"className":NclassName,
		"color": color,
		"dashStyle": dashStyle,
		"events": events,
		"id": id,
		"label": label,
		"value": value,
		"width": width,
		"zIndex": zIndex
	}

class BaseTitle(object):
	def __init__(self,):
		self.json = {
			"align": "center",
			"style": { "color": "#666666" },
			"text": None,
			"x": 0,
			"y": None,
		}

class SubTitle(BaseTitle):
	def __init__(self, align, style, text, x, y, useHTML, floating, verticalAlign, widthAdjust):
		super(__class__, self).__init__(align, style, text, x, y)
		options = {
			"useHTML": useHTML,
			"floating": floating,
			"verticalAlign": verticalAlign,
			"widthAdjust": widthAdjust,
		}
		self.json.update(options)

class Title(SubTitle):
	def __init__(self, align, style, text, x, y, useHTML, floating, margin, verticalAlign, widthAdjust):
		super(__class__, self).__init__(align, style, text, x, y, useHTML, floating, verticalAlign, widthAdjust))
		options = {
			"margin": margin
		}
		self.json.update(options)


class AxisTitle(BaseTitle):
	def __init__(self, align, style, text, x, y, enabled, margin, offset, reserveSpace, rotation):
		super(__class__, self).__init__(align, style, text, x, y)
		options = {
			"enabled": enabled,
			"margin": margin,
			"offset": offset,
			"reserveSpace": reserveSpace,
			"rotation": rotation,
		}
		self.json.update(options)

class Break(object):
	def __init__(self, breakSize, from_, repeat, to):
		self.json = {
			"breakSize":  breakSize,
			"from": from_,
			"repeat":  repeat,
			"to": to
		},


class Crosshair(object):
	def __init__(self, className, color, dashStyle, snap, width, zIndex):
		self.json = {
			"className": className,
			"color":  color,
			"dashStyle": dashStyle,
			"snap":  snap,
			"width": width,
			"zIndex":  zIndex,
		}


"chart": {
	"alignTicks": True,
	"animation": True,
	"backgroundColor": "#FFFFFF",
	"borderColor": "#335cad",
	"borderRadius": 0,
	"borderWidth": 0,
	"className": None,
	"colorCount": 10,
	"defaultSeriesType": "line",
	"description": None,
	"events": { 
		"addSeries": None,
		"afterPrint": None,
		"beforePrint": None,
		"click": None,
		"drilldown": None,
		"drillup": None,
		"drillupall": None,
		"load": None,
		"redraw": None,
		"render": None,
		"selection": None
	},
	"height": None,
	"ignoreHiddenSeries": True,
	"inverted": False,
	"margin": None,
	"marginBottom": None,
	"marginLeft": None,
	"marginRight": None,
	"marginTop": None,
#	"options3d": { },
	"panKey": None,
	"panning": False,
	"pinchType": None,
	"plotBackgroundColor": None,
	"plotBackgroundImage": None,
	"plotBorderColor": "#cccccc",
	"plotBorderWidth": 0,
	"plotShadow": False,
	"polar": False,
	"reflow": True,
	"renderTo": None,
#	"resetZoomButton": { },
	"selectionMarkerFill": "rgba(51,92,173,0.25)",
	"shadow": False,
	"showAxes": False,
	"spacing": [10, 10, 15, 10],
	"spacingBottom": 15,
	"spacingLeft": 10,
	"spacingRight": 10,
	"spacingTop": 10,
	"style": Style(fontFamily="\"Lucida Grande\", \"Lucida Sans Unicode\", Verdana, Arial, Helvetica, sans-serif", fontSize="12px"),
	"type": "line",
	"typeDescription": None,
	"width": None,
	"zoomType": None,
}

"credits": {
	"enabled": True,
	"href": "http://www.highcharts.com",
	"position": Position(align="right", verticalAlign="bottom",	x=-10, y=-5).json
	"style": Style(cursor="pointer", color="#999999",  fontSize="10px"),
	"text": "Highcharts.com",
}

"data": {
	"columns":None,
	"complete":None,
	"csv": None,
	"dateFormat": None,
	"decimalPoint": ".",
	"endColumn":None,
	"endRow":None,
	"firstRowAsNames": True,
	"googleSpreadsheetKey":None,
	"googleSpreadsheetWorksheet": None,
	"itemDelimiter":None,
	"lineDelimiter": "\n",
	"parseDate":None,
	"parsed":None,
	"rows":None,
	"seriesMapping": None,
	"startColumn": 0,
	"startRow": 0,
	"switchRowsAndColumns": False,
	"table":None,
}

"labels": {
	"items": [{
		"html": None,
		"style": None
	}],
	"style": Style(color="#333333")
}

"legend": {
	"align": "center", 
	"backgroundColor": None, 
	"borderColor": "#999999", 
	"borderRadius": 0, 
	"borderWidth": 0, 
	"enabled": True, 
	"floating": False, 
	"itemDistance": 20, 
	"itemHiddenStyle": { "color": "#cccccc" }, 
	"itemHoverStyle": { "color": "#000000" }, 
	"itemMarginBottom": 0, 
	"itemMarginTop": 0, 
	"itemStyle": Style(color="#333333", cursor="pointer", fontSize="12px", fontWeight="bold"), 
	"itemWidth": None, 
	"labelFormat": "{name}", 
	"labelFormatter": None, 
	"layout": "horizontal", 
	"lineHeight": 16, 
	"margin": 12, 
	"maxHeight": None, 
	"navigation": {
		"activeColor": "#003399", 
		"animation": True, 
		"arrowSize": 12, 
		"enabled": True, 
		"inactiveColor": "#cccccc", 
		"style": None
	}, 
	"padding": 8, 
	"reversed": False, 
	"rtl": False, 
	"shadow": False, 
	"squareSymbol": True, 
	"style": None, 
	"symbolHeight": None, 
	"symbolPadding": 5, 
	"symbolRadius": None, 
	"symbolWidth": None, 
	"title": {
		"style": {"fontWeight":"bold"}, 
		"text": None
	}, 
	"useHTML": False, 
	"verticalAlign": "bottom", 
	"width": None, 
	"x": 0, 
	"y": 0, 
}

"subtitle": SubTitle(align="center", floating=False, style={ "color": "#666666" }, text=None, useHTML=False, verticalAlign=" ", widthAdjust=-44, x=0, y=None)
"title": Title(align="center", floating=False, margin=15, style=Style(color="#333333", fontSize="18px"), text="Chart title", useHTML=False, verticalAlign=None, widthAdjust=-44, x=0, y=None)

"tooltip": {
	"animation": True,
	"backgroundColor": "rgba(247,247,247,0.85)",
	"borderColor": None,
	"borderRadius": 3,
	"borderWidth": 1,
	"crosshairs": None,
	"dateTimeLabelFormats": None,
	"enabled": True,
	"followPointer": False,
	"followTouchMove": True,
	"footerFormat": "False",
	"formatter": None,
	"headerFormat":None,
	"hideDelay": 500,
	"padding": 8,
	"pointFormat": "<span style=\"color\":{point.color}\">\u25CF</span> {series.\"name}\": <b>{point.y}</b><br/>",
	"pointFormatter":None,
	"positioner": None,
	"shadow": True,
	"shape": "callout",
	"shared": False,
	"snap": None,
	"split": False,
	"style": Style(color="#333333", cursor="default", fontSize="12px", pointerEvents="none", whiteSpace="nowrap"),
	"useHTML": False,
	"valueDecimals": None,
	"valuePrefix": None,
	"valueSuffix": None,
	"xDateFormat": None,
}

"xAxis": [{
	"allowDecimals": True,
	"alternateGridColor": None,
	"breaks": [Break(breakSize=0, from_=None, repeat=0, to=None)]
	"categories": None,
	"ceiling":None,
	"className":None,
	"crosshair": Crosshair(className=None, color=None, dashStyle="Solid", snap=True, width=None, zIndex=2),
	"dateTimeLabelFormats": None,
	"description": None,
	"endOnTick": False,
	"events": {…},
	"floor": None,
	"gridLineColor": "#e6e6e6",
	"gridLineDashStyle": "Solid",
	"gridLineWidth": 0,
	"gridZIndex": 1,
	"id": None,
	"labels": Labels(align=None, autoRotation=[-45], autoRotationLimit=80, distance=15, enabled=True, format="{value}", formatter=None, maxStaggerLines=5, 
		             overflow=None, padding=5, reserveSpace=True, rotation=0, staggerLines=None, step=None, style=Style(color="#666666", cursor="default", fontSize="11px"), 
		             useHTML=False, x=0, y=None, zIndex=7)
	"lineColor": "#ccd6eb",
	"lineWidth": 1,
	"linkedTo": None,
	"max": None,
	"maxPadding": 0.01,
	"maxZoom": None,
	"min": None,
	"minPadding": 0.01,
	"minRange": None,
	"minTickInterval": None,
	"minorGridLineColor": "#f2f2f2",
	"minorGridLineDashStyle": "Solid",
	"minorGridLineWidth": 1,
	"minorTickColor": "#999999",
	"minorTickInterval": None,
	"minorTickLength": 2,
	"minorTickPosition": "outside",
	"minorTickWidth": 0,
	"offset": 0,
	"opposite": False,
	"plotBands": [PlotBand(borderColor=None, borderWidth=0, className=None, color=None, events=None, from_=None, id=None, 
		          label=Label(align="center", rotation=0, style=None, text=None, textAlign= None, useHTML=False, verticalAlign="top", x=None, y=None), 
		          to=None, zIndex=None)],
	"plotLines": [PlotLine(className=None, color=None, dashStyle="Solid", events=None, id=None, 
		                   label=Label(align="left", rotation=None, style= None, text=None, textAlign= None, useHTML=False, verticalAlign="top", x=None, y=None), 
		                   value=None, width=None, zIndex=None)],
	"reversed": False,
	"showEmpty": True,
	"showFirstLabel": True,
	"showLastLabel": True,
	"softMax": None,
	"softMin": None,
	"startOfWeek": 1,
	"startOnTick": False,
	"tickAmount": None,
	"tickColor": "#ccd6eb",
	"tickInterval": None,
	"tickLength": 10,
	"tickPixelInterval": None,
	"tickPosition": "outside",
	"tickPositioner": None,
	"tickPositions": None,
	"tickWidth": 1,
	"tickmarkPlacement": None,
	"title": AxisTitle( align="middle", enabled="middle", margin=None, offset=None, reserveSpace=True, rotation=0, style=Style(color="#666666"), text=None, x=0, y=0)
	"type": "linear",
	"uniqueNames": True,
	"units":None,
	"visible": True,
}]


"yAxis": [{
	"allowDecimals": True,
	"alternateGridColor": None,
	"angle": 0,
	"breaks": [Break(breakSize=0, from_=None, repeat=0, to=None)]
	"categories": None,
	"ceiling":None,
	"className":None,
	"crosshair": Crosshair(className=None, color=None, dashStyle="Solid", snap=True, width=None, zIndex=2),
	"dateTimeLabelFormats": None,
	"description": None,
	"endOnTick": True,
	"events": {…},
	"floor": None,
	"gridLineColor": "#e6e6e6",
	"gridLineDashStyle": "Solid",
	"gridLineInterpolation": None,
	"gridLineWidth": 1,
	"gridZIndex": 1,
	"id": None,
	"labels": Labels(align="right", autoRotation=[-45], autoRotationLimit=80, distance=-25, enabled=True, format="{value}", formatter=None, maxStaggerLines=5, 
		             overflow=None, padding=5, reserveSpace=True, rotation=0, staggerLines=None, step=None, style=Style(color="#666666", cursor="default", fontSize="11px"), 
		             useHTML=False, x=0, y=None, zIndex=7)
	"lineColor": "#ccd6eb",
	"lineWidth": 0,
	"linkedTo": None,
	"max": None,
	"maxColor": "#003399",
	"maxPadding": 0.05,
	"maxZoom": None,
	"min": None,
	"minColor": "#e6ebf5",
	"minPadding": 0.05,
	"minRange": None,
	"minTickInterval": None,
	"minorGridLineColor": "#f2f2f2",
	"minorGridLineDashStyle": "Solid",
	"minorGridLineWidth": 1,
	"minorTickColor": "#999999",
	"minorTickInterval": None,
	"minorTickLength": 2,
	"minorTickPosition": "outside",
	"minorTickWidth": 0,
	"offset": 0,
	"opposite": False,
	"plotBands": [PlotBand(borderColor=None, borderWidth=0, className=None, color=None, events=None, from_=None, id=None, 
		          label=Label(align="center", rotation=0, style=None, text=None, textAlign= None, useHTML=False, verticalAlign="top", x=None, y=None), 
		          to=None, zIndex=None)],
	"plotLines": [PlotLine(className=None, color=None, dashStyle="Solid", events=None, id=None, 
		                   label=Label(align="left", rotation=None, style= None, text=None, textAlign= None, useHTML=False, verticalAlign="top", x=None, y=None), 
		                   value=None, width=None, zIndex=None)],
	"reversed": False,
	"reversedStacks": True,
	"showEmpty": True,
	"showFirstLabel": True,
	"showLastLabel": None,
	"softMax": None,
	"softMin": None,
	"stackLabels": {
		"align": None,
		"enabled": False,
		"format": "{total}",
		"formatter": None,
		"rotation": 0,
		"style": Style(color="#000000", fontSize="11px", fontWeight="bold", textShadow="1px 1px contrast, -1px -1px contrast, -1px 1px contrast, 1px -1px contrast"),
		"textAlign": None,
		"useHTML": False,
		"verticalAlign": None,
		"x": None,
		"y": None,
	},
	"startOfWeek": 1,
	"startOnTick": True,
	"stops": None,
	"tickAmount": None,
	"tickColor": "#ccd6eb",
	"tickInterval": None,
	"tickLength": 10,
	"tickPixelInterval": None,
	"tickPosition": "outside",
	"tickPositioner": None,
	"tickPositions": None,
	"tickWidth": 0,
	"tickmarkPlacement": None,
	"title": AxisTitle( align="middle", enabled="middle", margin=40, offset=None, reserveSpace=True, rotation=270, style=Style(color="#666666"), text="Values", x=0, y=None)
	"type": "linear",
	"uniqueNames": True,
	"units":None,
	"visible": True,
}]



"zAxis": {
	"allowDecimals": True,
	"alternateGridColor": None,
	"categories": None,
	"ceiling":None,
	"className":None,
	"crosshair": Crosshair(className=None, color=None, dashStyle="Solid", snap=True, width=None, zIndex=2)
	"dateTimeLabelFormats": None,
	"description": None,
	"endOnTick": False,
	"events": {
		"afterBreaks": None,
		"afterSetExtremes": None,
		"pointBreak": None,
		"pointInBreak":None,
		"setExtremes": None,
	},
	"floor": None,
	"gridLineColor": "#e6e6e6",
	"gridLineDashStyle": "Solid",
	"gridLineWidth": 0,
	"gridZIndex": 1,
	"id": None,
	"labels": Labels(align=None, autoRotation=[-45], autoRotationLimit=80, distance=15, enabled=True, format="{value}", formatter=None, maxStaggerLines=5, 
		             overflow=None, padding=5, reserveSpace=True, rotation=0, staggerLines=None, step=None, style=Style(color="#666666", cursor="default", fontSize="11px"), 
		             useHTML=False, x=0, y=None, zIndex=7)
	"lineColor": "#ccd6eb",
	"lineWidth": 1,
	"linkedTo": None,
	"max": None,
	"maxPadding": 0.01,
	"maxZoom": None,
	"min": None,
	"minPadding": 0.01,
	"minRange": None,
	"minTickInterval": None,
	"minorGridLineColor": "#f2f2f2",
	"minorGridLineDashStyle": "Solid",
	"minorGridLineWidth": 1,
	"minorTickColor": "#999999",
	"minorTickInterval": None,
	"minorTickLength": 2,
	"minorTickPosition": "outside",
	"minorTickWidth": 0,
	"offset": 0,
	"opposite": False,
	"plotBands": [PlotBand(borderColor=None, borderWidth=0, className=None, color=None, events=None, from_=None, id=None, 
		          label=Label(align="center", rotation=0, style=None, text=None, textAlign= None, useHTML=False, verticalAlign="top", x=None, y=None), 
		          to=None, zIndex=None)],
	"plotLines": [PlotLine(className=None, color=None, dashStyle="Solid", events=None, id=None, 
		                   label=Label(align="left", rotation=None, style= None, text=None, textAlign= None, useHTML=False, verticalAlign="top", x=None, y=None), 
		                   value=None, width=None, zIndex=None)],
	"reversed": False,
	"showEmpty": True,
	"showFirstLabel": True,
	"showLastLabel": True,
	"softMax": None,
	"softMin": None,
	"startOfWeek": 1,
	"startOnTick": False,
	"tickAmount": None,
	"tickColor": "#ccd6eb",
	"tickInterval": None,
	"tickLength": 10,
	"tickPixelInterval": None,
	"tickPosition": "outside",
	"tickPositioner": None,
	"tickPositions": None,
	"tickWidth": 1,
	"tickmarkPlacement": None,
	"title": AxisTitle(align="middle", enabled="middle", margin=None, offset=None, reserveSpace=True, rotation=0, style=Style(color="#666666"), text=None, x=0, y=None),
	"type": "linear",
	"uniqueNames": True,
	"units":None,
	"visible": True,
}