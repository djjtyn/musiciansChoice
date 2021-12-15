from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_form, name = 'payment_form'),
    path('create_payment_intent', views.create_payment_intent, name = 'create_payment_intent'),
    path('payment_fail', views.payment_fail, name = 'payment_fail'),
    #path('paymentSuccess', views.display_payment_success, name = 'payment_success'),
]