from django.shortcuts import render
from instruments.models import Instrument
from django.conf import settings

# Method to display the application home page
def display_home_page(request):
    access_key = settings.AWS_ACCESS_KEY_ID
    # Gather recommendations
    return render(request, 'index.html', {'key': access_key})
