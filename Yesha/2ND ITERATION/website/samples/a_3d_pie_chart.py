from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from sample.fusioncharts import FusionCharts

from sample.models import *

# Loading Data from a Static JSON String
# It is a example to show a Pie 3D chart where data is passed as JSON string format.
# The `chart` method is defined to load chart data from an JSON string.

booking = ReviewSites.objects.filter(site="booking").count()
agoda = ReviewSites.objects.filter(site="agoda").count()

def chart(request):
    # Create an object for the pie3d chart using the FusionCharts class constructor
  pie3d = FusionCharts("pie3d", "ex2" , "100%", "400", "chart-1", "json", 
        # The data is passed as a string in the `dataSource` as parameter.
    """{ 
            "chart": {
            "caption": "Age profile of website visitors",
            "subcaption": "Last Year",
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
                    "value": 1449 
                },{
                    "label": "Agoda", 
                    "value": 1343
                },{
                    "label": "TripAdvisor", 
                    "value": "100"
                }
            ]
    }""")
  
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
  return  render(request, 'index.html', {'output' : pie3d.render()})
