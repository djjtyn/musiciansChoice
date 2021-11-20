from django.db import models

# Import foreign keys
from instruments.models import Instrument
from users.models import CustomUser

class Comment(models.Model):
    comment = models.CharField(max_length = 4000)
    instrument = models.ForeignKey(Instrument, on_delete = models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.comment