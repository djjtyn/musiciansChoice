from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('home.urls')),
    path('users/', include('users.urls')),
    path('addSupplier', include('brands.urls')),
    path('addInstrumentType', include('instrument_type.urls')),
    path('instruments/', include('instruments.urls')),
    path('admin/', admin.site.urls),
]
