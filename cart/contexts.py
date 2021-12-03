# This file is used to allow the cart details to be viewed on any page
from instruments.models import Instrument

def cart(request):
    # Initialise an empty cart if a cart doesn't exist
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        instrument = Instrument.objects.get(pk = id)
        total += quantity * instrument.cost
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'instrument':instrument, 'subTotal': quantity * instrument.cost})
    return { 'cart_items':cart_items, 'total': total, 'product_count': product_count}
    
