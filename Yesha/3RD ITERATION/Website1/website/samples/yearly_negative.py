from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from sample.fusioncharts import FusionCharts

from sample.models import *

# The `chart` function is defined to load data from a Python Dictionary. This data will be converted to
# JSON and the chart will be rendered.

def chart(request):
	# Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
	dataSource = {}
	dataSource['chart'] = {
		"caption" : "2017 NEGATIVE REVIEWS",
	    "paletteColors" : "#c24d00",
	    "bgColor" : "#ffffff",
	    "borderAlpha": "20",
	    "canvasBorderAlpha": "0",
	    "usePlotGradientColor": "0",
	    "plotBorderAlpha": "10",
	    "showXAxisLine": "1",
	    "xAxisLineColor" : "#999999",
	    "showValues" : "0",
	    "divlineColor" : "#999999",
	    "divLineIsDashed" : "1",
	    "showAlternateHGridColor" : "0"
		}

    # Convert the data in the `actualData` array into a format that can be consumed by FusionCharts.
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

	dataSource['data'] = []
    # Iterate through the data in `Country` model and insert in to the `dataSource['data']` list.

	for key in Monthly.objects.filter(year = "2016"):
		data = {}
		data['label'] = key.month + key.year
		data['value'] = (int(key.total_neg) / (int(key.total_pos) + int(key.total_neg))) * 100
		dataSource['data'].append(data)

    # Create an object for the Column 2D chart using the FusionCharts class constructor
	column2D = FusionCharts("column2D", "ex1" , "1350", "400", "chart-1", "json", dataSource)


	return render(request, 'index.html', {'output_1': column2D.render()})








