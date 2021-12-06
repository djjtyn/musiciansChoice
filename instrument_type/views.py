from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from.models import InstrumentType
from django.contrib import messages

# This method will only be invoked if the user is a logged in staff member
@staff_member_required
def instrument_type_form(request):
    # get all the current suppliers 
    instrument_types = InstrumentType.objects.all().order_by('type')
    # If the form has been submitted
    if request.method == "POST":
        try:
            new_instrument_type = request.POST.get('instrument_type')
            # check if the instrument type already exists
            if InstrumentType.objects.filter(type__iexact = new_instrument_type).exists():
                messages.info(request, f"{new_instrument_type} already exists in the database")
            else:
                # if the instrument type doesn't already exist instantiate the InstrumentType class 
                try:
                    new_type = InstrumentType()
                    new_type.type = new_instrument_type
                    new_type.save()
                    messages.info(request, f"{new_instrument_type} has been added to the database")
                except:
                    messages.info(request, "There was an issue adding this to the database")
        except:
            messages.info(request, "There was an issue processing the request")
    return render (request, "instrumentTypeForm.html", {'instrument_types': instrument_types})


