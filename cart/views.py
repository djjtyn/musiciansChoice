from django.shortcuts import render
from django.contrib import messages
import os

import stripe
import json

# Display cart contents
def view_cart(request):
    cart = request.session.get('cart', {})
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
    cart[instrument_id] = quantity
    # # Check if item is already in cart
    # if quantity > 0:
    #     cart[instrument_id] = quantity
    request.session['cart'] = cart
    messages.success(request, "Your cart is now empty")
    return render(request, 'cart.html')
    

    
