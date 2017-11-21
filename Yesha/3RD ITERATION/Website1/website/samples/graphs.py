from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from sample.fusioncharts import FusionCharts

from sample.models import *
# Loading Data from a Static JSON String
# Example to create a Angular Gauge with the chart data passed as JSON string format.
# The `chart` method is defined to load chart data from a JSON string.

def chart(request):
    # REVIEWS PER WEBSITE
    booking = ReviewSites.objects.filter(site="booking").count()
    agoda = ReviewSites.objects.filter(site="agoda").count()
    pie3d = FusionCharts("pie3d", "ex2", "500", "270", "chart-1", "json",
                         # The data is passed as a string in the `dataSource` as parameter.
                         """{ 
                                 "chart": {
                                 "caption": "REVIEWS PER WEBSITE",
                                 "subcaption": "Agoda | Booking | TripAdvisor",
                                 "startingangle": "120",
                                 "showlabels": "0",
                                 "showlegend": "1",
                                 "enablemultislicing": "0",
                                 "slicingdistance": "15",
                                 "showpercentvalues": "1",
                                 "showpercentintooltip": "0",
                                 "plottooltext": "$label Total Data : $datavalue",
                                 "theme": "ocean"
                                 },

                                 "data": [
                                     {
                                         "label": "Booking", 
                                         "value":""" + str(booking) + """
                       },{
                           "label": "Agoda", 
                           "value": """ + str(agoda) + """
                       },{
                           "label": "TripAdvisor", 
                           "value": "100"
                       }
                   ]
           }""")


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
        "bgcolor": "white",
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



    dataSource2 = {}

    # Chart data is passed to the `dataSource2` parameter, as hashes, in the form of
    # key-value pairs.
    dataSource2['chart'] = {
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

    dataSource2["categories"] = [{
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

    # Iterate through the data in `Country` model and insert in to the `dataSource2['data']` list.
    value_neg = []
    value_pos = []
    for key in Monthly.objects.filter(year="2017"):
        value_neg.append((int(key.total_neg) / (int(key.total_neg) + int(key.total_pos))) * 100)
        value_pos.append((int(key.total_pos) / (int(key.total_neg) + int(key.total_pos))) * 100)

    dataSource2["dataset"] = [{
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
    angularGauge = FusionCharts("angulargauge", "ex1", "450", "270", "chart-2", "json", datasource)
    stackedcolumn2d = FusionCharts("stackedcolumn2d", "ex1", "700", "300", "chart-3", "json", dataSource2)

    return  render(request, 'index2.html', {'output_1': pie3d.render(),
                                            'output_2': angularGauge.render(),
                                            'output_3': stackedcolumn2d.render()})

