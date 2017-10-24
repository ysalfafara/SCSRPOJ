from django.conf.urls import include, url
from django.contrib import admin
from samples import database_example

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sample/', include('sample.urls')),
    url(r'^database-example/', database_example.chart, name='chart'),
]
