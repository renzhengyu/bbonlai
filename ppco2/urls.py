from django.urls import path
from . import views


app_name = 'ppco2'
urlpatterns = [
    path('', views.cfp_vue, name='vue_form'),
    path('analysis/', views.planet_chart, name='planet_chart'),
    path('analysis/data/', views.planet_chart_data, name='planet_chart_data'),
]
