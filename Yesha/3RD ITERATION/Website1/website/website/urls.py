from django.conf.urls import include, url
from django.contrib import admin
from samples import yearly_positive, graphs
from samples import yearly_negative, piechart_3d
from samples import angular_gauge, percentage_2017
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graphs/', graphs.chart, name='chart'),
    url(r'^percentage_2017/', percentage_2017.chart, name='chart'),
    url(r'^3d_piechart/', piechart_3d.chart, name='chart'),
    url(r'^angular_gauge/', angular_gauge.chart, name='chart'),
    url(r'^yearly_positive/', yearly_positive.chart, name='chart'),
    url(r'^yearly_negative/', yearly_negative.chart, name='__main__'),
]
