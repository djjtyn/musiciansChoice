from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from .forms import InstrumentForm
from brands.models import Brand
from instrument_type.models import InstrumentType
from django.contrib import messages
from .models import Instrument
import traceback



# This method will only be invoked if the user is a logged in staff member
@staff_member_required
def product_form(request):
    # If the ofrm has been submitted
    if request.method == "POST":
        try:
            # Get the brand and instrument type instances
            brand = Brand.objects.get(pk = request.POST.get('brand'))
            type = InstrumentType.objects.get(pk = request.POST.get('type'))
            instrument = Instrument()
            instrument.name = request.POST.get('model')
            instrument.description = request.POST.get('description')
            instrument.stock_amount = request.POST.get('stock')
            instrument.cost = request.POST.get('price')
            instrument.instrument_type = type
            instrument.brand = brand
            instrument.save()
        except:
            messages.info(request, "There was an issue creating this instrument")
            traceback.print_exc()
    # If the request is a get request get all the product brands and instrument types already in the db
    brands = Brand.objects.all().order_by('brand')
    # Get all the instrument types already in the db
    types = InstrumentType.objects.all().order_by('type')
    return render(request, "InstrumentForm.html", {'brands': brands, 'types': types})
    
def view_instruments(request):
    # Get all the instruments from the database
    instruments = Instrument.objects.all().order_by('cost')
    return render(request, "instruments.html", {'instruments' : instruments});
