from django.shortcuts import render
from instruments.models import Instrument

# Method to display the application home page
def display_home_page(request):
    # Gather recommendations
    return render(request, 'index.html')
