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
    pie3d = FusionCharts("pie3d", "ex2", "100%", "400", "chart-1", "json",
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
                                 "plottooltext": "Age group : $label Total visit : $datavalue",
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

    angularGauge = FusionCharts("angulargauge", "ex1", "450", "270", "chart-2", "json", datasource)


    return  render(request, 'index.html', {'output_1' : angularGauge.render(),
                                           'output_2': pie3d.render()})

