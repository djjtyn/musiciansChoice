from django.urls import path
from . import views

app_name = 'instrument'
urlpatterns = [
    path('add', views.product_form, name = 'product_form'),
    path('view', views.view_instruments, name = 'view_instruments'),
    path('view/<int:instrument_id>', views.view, name = 'view'),
    path('adjust_stock/<int:instrument_id>', views.adjust_stock, name = 'adjust_stock'),
]