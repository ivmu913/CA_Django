from django.urls import path
from . import views

# LIBRARY APP
urlpatterns  = [
    path('', views.index, name='index')
]
