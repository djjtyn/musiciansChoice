from django.urls import path
from . import views

app_name = 'sns_notifications'
urlpatterns = [
    path('<int:instrument_id>', views.notify_when_product_is_back_in_stock, name = 'stock_notify'),
]