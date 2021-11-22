from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import InstrumentForm
from brands.models import Brand
from instrument_type.models import InstrumentType


# Method below will address the orm required to add a new instrument to the db by admin users
@login_required()
def product_form(request):
    # Get all the products brands already in the db
    brands = Brand.objects.all().order_by('brand')
    # Get all the instrument types already in the db
    types = InstrumentType.objects.all().order_by('type')
    
    return render(request, "InstrumentForm.html", {'brands': brands, 'types': types})
