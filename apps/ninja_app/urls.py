from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^processmoney$', views.processmoney),
    # url(r'^confirm$', views.confirm),
    # url(r'^clear$', views.clear)
    ]