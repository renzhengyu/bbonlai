from django.urls import path
from . import views


app_name = 'ppco2'
urlpatterns = [
    path('', views.CfpWizard.as_view(), name='formseven'),
    path('analysis/', views.planet_chart, name='planet_chart'),
    path('analysis/data/', views.planet_chart_data, name='planet_chart_data'),
    path('result/<int:pk>/', views.cal_result, name='cal_result')
]
