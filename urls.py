from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView

urlpatterns = [

    url(r'^fib$',views.index, name='index'),
    url(r'^fib/result$', views.fibview, name='fibview'),
]





