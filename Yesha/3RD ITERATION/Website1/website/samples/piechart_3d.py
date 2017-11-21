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


    return render(request, 'index.html', {'output':  pie3d.render()})