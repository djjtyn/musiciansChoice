from django.urls import path
from . import views

app_name = 'instrument'
urlpatterns = [
    path('add', views.product_form, name = 'product_form'),
    path('view', views.view_instruments, name = 'view_instruments'),
    path('view/recommendations', views.view_recommendations, name = 'view_recommendations'),
    path('view/<int:instrument_id>', views.view, name = 'view'),
    path('edit/<int:instrument_id>', views.edit, name = 'edit'),
    path('adjust_stock/<int:instrument_id>', views.adjust_stock, name = 'adjust_stock'),
]