from django.urls import path
from . import views

urlpatterns = [
    path('', views.instrument_type_form, name = 'instrument_type_form'),
]