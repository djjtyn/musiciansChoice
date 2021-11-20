from django.db import models

class InstrumentType(models.Model):
    type = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.type
