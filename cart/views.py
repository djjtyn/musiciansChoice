from django.shortcuts import render, redirect
from django.contrib import messages
import os
import traceback
from django.conf import settings

import stripe
import json

# Display cart contents
def view_cart(request):
    s3_bucket_url =  settings.INSTRUMENT_IMAGE_URL
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', {'bucket': s3_bucket_url})
    
# Empty cart contents
def empty_cart(request):
    request.session['cart'] = {}
    messages.success(request, "Your cart is now empty")
    return render (request, "cart.html")
    
    
def add_to_cart(request, instrument_id):
    try:
        quantity = int(request.POST.get('quantity'))
        #If no cart exists, create a cart, else retrieve existing cart
        cart = request.session.get('cart',{})
        if quantity > 0:
            # Determine if the instrument is already in the cart, add to it's quantity if it is
            if str(instrument_id) in cart:
                cart[str(instrument_id)] += quantity
            else:
                cart[instrument_id] = quantity
            if quantity == 1:
                    messages.info(request, "Item added to cart")
            if quantity > 1:
                    messages.info(request, f"{quantity} items added to cart")
    except: 
        messages.info(request, "An error occurred adding this item")
    request.session['cart'] = cart
    return redirect ('instrument:view_instruments')
    
def adjust_cart(request, instrument_id):
    quantity = int(request.POST.get('quantity'))
    # Get the item from the cart and adjust to the value submitted in the form
    cart = request.session.get('cart',{})
    cart[str(instrument_id)] = quantity
    request.session['cart'] = cart
    messages.success(request, "Your cart has been adjusted")
    return render(request, 'cart.html')

    
