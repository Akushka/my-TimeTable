from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.TableTime_list, name='TableTime_list'),
]