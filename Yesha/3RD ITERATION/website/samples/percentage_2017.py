from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from sample.fusioncharts import FusionCharts

from sample.models import *


def chart(request):
	dataSource = {}

	# Chart data is passed to the `dataSource` parameter, as hashes, in the form of
	# key-value pairs.
	dataSource['chart'] = {
		"caption": "Sentiment Analysis for the Year 2017",
        "subCaption": "Agoda | Booking | TripAdvisor",
    	"xAxisname": "Month",
        "yAxisName": "Sentiment",
        "numberSuffix": "%",
        "paletteColors": "6BAA01,008EE4",
        "bgAlpha": "0",
        "borderAlpha": "20",
        "canvasBorderAlpha": "0",
        "usePlotGradientColor": "0",
        "plotBorderAlpha": "10",
        "legendBorderAlpha": "0",
        "legendShadow": "0",
        "valueFontColor": "FFFFFF",
        "captionpadding": "20",
        "showAxisLines": "1",
        "axisLineAlpha": "25",
	}

	dataSource["categories"] = [{
		"category": [
			{"label": "Jan"},
			{"label": "Feb"},
			{"label": "Mar"},
			{"label": "Apr"},
			{"label": "May"},
			{"label": "Jun"},
			{"label": "Jul"},
			{"label": "Aug"},
			{"label": "Sep"},
			{"label": "Oct"}
		]
	}]

	# Iterate through the data in `Country` model and insert in to the `dataSource['data']` list.
	value_neg = []
	value_pos = []
	for key in Monthly.objects.filter(year="2017"):
		value_neg.append((int(key.total_neg) / (int(key.total_neg) + int(key.total_pos))) * 100)
		value_pos.append((int(key.total_pos) / (int(key.total_neg) + int(key.total_pos))) * 100)


	dataSource["dataset"] = [{
		"seriesname": "Negative",
		"data": [
			{"value": str(int(value_neg[9]))},
			{"value": str(int(value_neg[8]))},
			{"value": str(int(value_neg[7]))},
			{"value": str(int(value_neg[6]))},
			{"value": str(int(value_neg[5]))},
			{"value": str(int(value_neg[4]))},
			{"value": str(int(value_neg[3]))},
			{"value": str(int(value_neg[2]))},
			{"value": str(int(value_neg[1]))},
			{"value": str(int(value_neg[0]))}
		]
	}, {
		"seriesname": "Positive",
		"data": [
			{"value": str(int(value_pos[9]))},
			{"value": str(int(value_pos[8]))},
			{"value": str(int(value_pos[7]))},
			{"value": str(int(value_pos[6]))},
			{"value": str(int(value_pos[5]))},
			{"value": str(int(value_pos[4]))},
			{"value": str(int(value_pos[3]))},
			{"value": str(int(value_pos[2]))},
			{"value": str(int(value_pos[1]))},
			{"value": str(int(value_pos[0]))}
		]
	}
	]

	# Create an object for the Multiseries column 2D charts using the FusionCharts class constructor
	mscol2D = FusionCharts("stackedcolumn2d", "ex1", "700", "300", "chart-1", "json", dataSource)
	return render(request, 'index.html', {'output_1': mscol2D.render()})