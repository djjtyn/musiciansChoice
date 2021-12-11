from django.shortcuts import render
from django.contrib import messages
import os

import stripe
import json

# Display cart contents
def view_cart(request):
    cart = request.session.get('cart', {})
    print(cart)
    return render(request, 'cart.html')
    
# Empty cart contents
def empty_cart(request):
    request.session['cart'] = {}
    messages.success(request, "Your cart is now empty")
    return render (request, "cart.html")
    
    
def add_to_cart(request, instrument_id):
    quantity = int(request.POST.get('quantity'))
    #If no cart exists, create a cart, else retrieve existing cart
    cart = request.session.get('cart',{})
    # Determine if the instrument is already in the cart, add to it's quantity if it is
    if str(instrument_id) in cart:
        cart[str(instrument_id)] += quantity
    else:
        cart[instrument_id] = quantity
    request.session['cart'] = cart
    messages.success(request, "Your cart is now empty")
    return render(request, 'cart.html')
    

    
