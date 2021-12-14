from django.shortcuts import render
from .models import Order

# Create your views here.
def view_orders(request):
    # If the user is a admin, display all others
    if request.user.is_admin:
        try:
            # Get all the orders from the database
            orders = Order.objects.all()
            print(orders)
        except:
            print("Issue retrieving the orders")
    else:
        # Get all the orders linked to the logged in user
        orders = Order.objects.filter(customer = request.user)
        print("Is not admin")
    return render(request, 'orders.html', {'orders': orders})