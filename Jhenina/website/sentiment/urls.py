from django.conf.urls import url
from . import views

urlpatterns = [
    # /sentiment/
    url(r'^$', views.index, name='index'),

    # /sentiment/1/
    url(r'^(?P<review_id>[0-9]+)$', views.detail, name='detail'),
]