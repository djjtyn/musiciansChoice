from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('view', views.view_cart, name = 'view_cart'),
    path('empty', views.empty_cart, name = 'empty_cart'),
    path('add/<int:instrument_id>', views.add_to_cart, name = 'add'),
    #path('create-checkout-session', views.invoke_stripe, name = 'invoke_stripe'),
]