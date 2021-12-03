from django.db import models

#import the classes used s foreign keys
from instrument_type.models import InstrumentType
from brands.models import Brand

class Instrument(models.Model):
    name = models.CharField(max_length = 60)
    description = models.CharField(max_length = 500)
    stock_amount = models.IntegerField()
    cost = models.FloatField()
    instrument_type = models.ForeignKey(InstrumentType, on_delete = models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    
    def __str__(self):
        return f"{self.brand} {self.name}" 
        
class InstrumentPicture(models.Model):
    pictureUrl = models.CharField(max_length = 2048)
    instrument = models.ForeignKey(Instrument, on_delete = models.CASCADE)
