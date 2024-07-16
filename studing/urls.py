from django.urls import path, re_path, register_converter
from . import views



app_name = 'studing'

urlpatterns = [

    path('', views.index, name='index'),

]
