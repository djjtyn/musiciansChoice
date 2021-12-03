from django.urls import path
from . import views

urlpatterns = [
    path('add', views.product_form, name = 'product_form'),
    path('view', views.view_instruments, name = 'view_instruments'),
]