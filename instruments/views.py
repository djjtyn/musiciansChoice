from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from brands.models import Brand
from instrument_type.models import InstrumentType
from django.contrib import messages
from .models import Instrument, InstrumentPicture
from sns_notifications.sns_utils import sns
import traceback
from django.conf import settings
from custom_library.library_methods_pkg.library_methods import MyMethods




# This method will only be invoked if the user is a logged in staff member
@staff_member_required
def product_form(request):
    # If the form has been submitted
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
            s3_bucket_url =  settings.INSTRUMENT_IMAGE_URL
            # If a picture was supplied in the form upload it to S3
            if request.POST.get('picture') != "":
                try:
                    instrumentPic = InstrumentPicture()
                    instrumentPic.instrument = instrument
                    instrumentPic.image = request.FILES['picture']
                    instrumentPic.save()
                except:
                    messages.info(request, "There was an issue creating this instrument")
                    traceback.print_exc()
            messages.info(request, "Product successfully uploaded")
            return render(request, "instrument.html", {'product': instrument, 'bucket': s3_bucket_url})
        except:
            messages.info(request, "There was an issue in the overall process")
            traceback.print_exc()
    # If the request is a get request get all the product brands and instrument types already in the db
    brands = Brand.objects.all().order_by('brand')
    # Get all the instrument types already in the db
    types = InstrumentType.objects.all().order_by('type')
    return render(request, "InstrumentForm.html", {'brands': brands, 'types': types})
    
def view_instruments(request):
    s3_bucket_url =  settings.INSTRUMENT_IMAGE_URL
    # Get all the instruments from the database
    instruments = list(Instrument.objects.all())
    testLib = MyMethods()
    testLib.sort_by(instruments, 0, len(instruments)-1 , "cost")
    instrument_images = InstrumentPicture.objects.all()
    return render(request, "instruments.html", {'instruments' : instruments, 'image': instrument_images, 'bucket': s3_bucket_url});
    
def view(request, instrument_id):
    s3_bucket_url =  settings.INSTRUMENT_IMAGE_URL
    # Retrieve the selected instruments details
    product = Instrument.objects.get(pk=instrument_id)
    return render(request, "instrument.html", {'product': product, 'bucket': s3_bucket_url})

@staff_member_required    
def adjust_stock(request, instrument_id):
    quantity = int(request.POST.get('quantity'))
    product = Instrument.objects.get(pk=instrument_id) 
    try:
        # Adjust the selected instruments stock amount using quantity value provided in form
        product.stock_amount = quantity
        product.save()
        messages.info(request, "Stock successfully adjusted")
    except:
        messages.info(request, "Issue adjusting product stock")
    try:
        # Publish to restock notification topic if it exists
        sns.publish_to_topic_and_remove_topic(f"restockNotificationForInstrumentId{instrument_id}", f"You are receiving this message because you have previously opted to receive a restock notification for the {product.brand.brand} {product.name} product range. Good news! We have just added {quantity} new stock for this!")
    except:
        traceback.print_exc()
        print("Issue publshing to any topic that exists for restock notification")
    return redirect ('instrument:view_instruments')

