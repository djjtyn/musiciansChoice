# This file is used to allow the cart details to be viewed on any page
from instruments.models import Instrument

def cart_contents(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    product_count = 0
    print(f"From Context: {cart.keys()}")
    if '1' in cart.keys():
        print("Exists")
    for id, quantity in cart.items():
        instrument  = Instrument.objects.get(pk = id)
        total += quantity * instrument.cost
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'instrument': instrument})
    return { 'cart_items':cart_items, 'total': total, 'product_count': product_count}
    
