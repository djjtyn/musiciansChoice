from django.db import models
#import the classes used as foreign keys
#from comments.models import UserComment
from instrument_type.models import InstrumentType
from brands.models import Brand
from users.models import CustomUser

# from comments.models import CommentModel

class Instrument(models.Model):
    name = models.CharField(max_length = 60)
    description = models.CharField(max_length = 500)
    stock_amount = models.IntegerField()
    cost = models.FloatField()
    instrument_type = models.ForeignKey(InstrumentType, on_delete = models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    
    def __str__(self):
        return f"{self.brand} {self.name}" 
        
    def get_image(self):
        return InstrumentPicture.objects.get(instrument = self.id)
        
    # def get_comments(self):
    #     return Comment.objects.filter(instrument = self.id)
        
    def get_sorting_filter(self, sorting_filter):
        if sorting_filter == "name":
            return self.name
        if sorting_filter == "stock_amount":
            return self.stock_amount
        if sorting_filter == "cost":
            return self.cost
        if sorting_filter == "brand":
            return self.brand.brand
        
class InstrumentPicture(models.Model):
    pictureUrl = models.CharField(max_length = 2048)
    image = models.ImageField(upload_to='img/')
    instrument = models.ForeignKey(Instrument, on_delete = models.CASCADE)
    
class InstrumentCmment(models.Model):
    comment = models.CharField(max_length = 6000)
    instrument = models.ForeignKey(Instrument, on_delete = models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    
