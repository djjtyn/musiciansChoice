from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Brand


# This method will only be invoked if the user is a logged in staff member
@staff_member_required
def supplier_form(request):
     # get all the current suppliers 
    suppliers = Brand.objects.all().order_by('brand')
    # If the for mhas been submitted
    if request.method == "POST":
        try:
            new_supplier = request.POST.get('supplier')
            # check if the supplier already exists
            if Brand.objects.filter(brand__iexact = new_supplier).exists():
                messages.info(request, f"{new_supplier} already exists in the database")
            else:
                # if the supplier doesn't already exist instantiate the Brand class 
                try:
                    supplier = Brand()
                    supplier.brand = new_supplier
                    supplier.save()
                    messages.info(request, f"{new_supplier} has been added to the database")
                except: 
                    messages.info(request, "There was an issue adding this to the database")
        except:
            messages.info(request, "There was an issue processing the request")
    return render (request, "supplierForm.html", {'suppliers': suppliers})

