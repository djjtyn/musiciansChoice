from django.shortcuts import render
from .models import Order
from django.contrib import messages
from musicians_choice_lib_pkg.musicians_choice_lib import MyMethods # Custom library

# Create your views here.
def view_orders(request):
    # If the user is a admin, display all others
    if request.user.is_admin:
        try:
            # Get all the orders from the database
            orders = list(Order.objects.all())
            print(orders)
        except:
            print("Issue retrieving the orders")
    else:
        # Get all the orders linked to the logged in user
        orders = list(Order.objects.filter(customer = request.user))
        # If the request is a post request a filter has been applied
    if request.method == "POST":
        # Determine if filter is a sort filter or another filter
        if request.POST.get('sort_by'):
            sort_filter = request.POST.get('sort_by')
            myLib = MyMethods()
            myLib.sort_by(orders, 0, len(orders)-1 , sort_filter)
            messages.info(request, f"Products sorted by {sort_filter}")
    return render(request, 'orders.html', {'orders': orders})