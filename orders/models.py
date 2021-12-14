from django.db import models

# Import foreign keys
from users.models import CustomUser
from instruments.models import Instrument

class Order(models.Model):
    date = models.DateTimeField(auto_now_add = True)
    totalCost = models.FloatField()
    delivery_street = models.CharField(max_length = 80)
    delivery_town = models.CharField(max_length = 28)
    delivery_county = models.CharField(max_length = 14)
    delivery_postcode = models.CharField(max_length = 9)
    customer_phone = models.CharField(max_length = 30)
    customer = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    
    def get_order_details(self):
        return OrderLineItem.objects.filter(order = self.id)

        

        
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null = False, on_delete = models.PROTECT)
    instrument = models.ForeignKey(Instrument, null = False, on_delete = models.PROTECT)
    quantity = models.IntegerField()
    
    def calculate_cost(self):
        return self.quantity * self.instrument.cost
    
    
    
