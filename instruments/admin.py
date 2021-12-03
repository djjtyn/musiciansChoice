from django.contrib import admin
from .models import Instrument, InstrumentPicture

# Register your models here.
admin.site.register(Instrument)
admin.site.register(InstrumentPicture)
