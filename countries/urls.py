from django.urls import path
from . import views

urlpatterns = [
    path('stats/', views.stats, name='stats'), 
    path('', views.countries_list, name='countries_list'),
    path('<str:cca3>/', views.country_detail, name='country_detail'),
    
]
