from django.urls import path
from . import views


urlpatterns = [
    path('', views.display_home_page, name = 'home'),
]
