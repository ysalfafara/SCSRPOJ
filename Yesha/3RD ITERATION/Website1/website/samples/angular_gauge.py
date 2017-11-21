from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from sample.fusioncharts import FusionCharts

from sample.models import *
# Loading Data from a Static JSON String
# Example to create a Angular Gauge with the chart data passed as JSON string format.
# The `chart` method is defined to load chart data from a JSON string.

def chart(request):
    #CUSTOMER SATISFACTION PERCENTAGE
    datasource = {}
    datasource["chart"] = {
        "caption": "Customer Satisfaction Percentage",
        "subcaption": "Agoda | Booking | TripAdvisor",
        "lowerlimit": "0",
        "upperlimit": "100",
        "lowerlimitdisplay": "Negative",
        "upperlimitdisplay": "Positive",
        "numbersuffix": "%",
        "tickvaluedistance": "10",
        "gaugeinnerradius": "0",
        "bgcolor": "FFFFFF",
        "pivotfillcolor": "333333",
        "pivotradius": "8",
        "pivotfillmix": "333333, 333333",
        "pivotfilltype": "radial",
        "pivotfillratio": "0,100",
        "showtickvalues": "1",
        "majorTMThickness": "2",
        "majorTMHeight": "15",
        "minorTMHeight": "3",
        "showborder": "0",
        "plottooltext": "<div>Average Score : <b>$value%</b></div>",
    }
    datasource["colorrange"] = {
        "color": [{
              "minvalue": "0",
              "maxvalue": "50",
              "code": "e44a00"
        }, {
              "minvalue": "50",
              "maxvalue": "75",
              "code": "f8bd19"
        }, {
              "minvalue": "75",
              "maxvalue": "100",
              "code": "6baa01"
        }]
    }

    total = ReviewSites.objects.filter(sentiment = "pos").count()
    all_reviews = ReviewSites.objects.all().count()
    total = (total / all_reviews) * 100
    datasource["dials"] = {
        "dial": [{
            "value": str(total),
            "tooltext": "Total : $value",
            "rearextension": "15",
            "radius": "100",
            "bgcolor": "333333",
            "bordercolor": "333333",
            "basewidth": "8"
        }]
    }

    angularGauge = FusionCharts("angulargauge", "ex1", "450", "270", "chart-1", "json", datasource)

    cylinderChart = FusionCharts("cylinder", "ex2", "100%", "200", "chart-2", "json",
                                 # The chart data is passed as a string to the `dataSource` parameter.
                                 """{
                                     "chart": {
                                         "manageresize": "1",
                                         "bgcolor": "FFFFFF",
                                         "bgalpha": "0",
                                         "showborder": "0",
                                         "lowerlimit": "0",
                                         "upperlimit": "100",
                                         "showtickmarks": "0",
                                         "showtickvalues": "0",
                                         "showlimits": "0",
                                         "numbersuffix": "%",
                                         "decmials": "0",
                                         "cylfillcolor": "CC0000",
                                         "basefontcolor": "CC0000",
                                         "chartleftmargin": "15",
                                         "chartrightmargin": "15",
                                         "charttopmargin": "15"
                                     },
                                     "value": """  """,
                                     "annotations": {
                                         "groups": [
                                             {
                                                 "showbelow": "1",
                                                 "items": [
                                                     {
                                                         "type": "rectangle",
                                                         "x": "$chartStartX+1",
                                                         "y": "$chartStartY+1",
                                                         "tox": "$chartEndX-1",
                                                         "toy": "$chartEndY-1",
                                                         "color": "FFFFFF",
                                                         "alpha": "100",
                                                         "showborder": "0",
                                                         "bordercolor": "CC0000",
                                                         "borderthickness": "2",
                                                         "radius": "10"
                                                     }
                                                 ]
                                             }
                                         ]
                                     }
                                 }""")

    return  render(request, 'index.html', {'output' : angularGauge.render()})

