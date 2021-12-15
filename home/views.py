from django.shortcuts import render
from instruments.models import Instrument
from django.conf import settings
# Method to display the application home page
def display_home_page(request):
    print(settings.STRIPE_PUBLISHABLE_KEY)
    # Gather recommendations
    return render(request, 'index.html')
