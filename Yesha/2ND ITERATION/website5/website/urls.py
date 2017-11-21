from django.conf.urls import include, url
from django.contrib import admin
from samples import database_example, angular_gauge_example
from samples import a_3d_pie_chart
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sample/', include('sample.urls')),
    url(r'^database-example/', database_example.chart, name='chart'),
    url(r'^angular-gauge-example/', angular_gauge_example.chart, name='chart'),
    url(r'^render-3d-pie-chart/', a_3d_pie_chart.chart, name='chart'),
]
