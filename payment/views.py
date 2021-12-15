from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from instruments.models import Instrument
from users.models import CustomUser
from orders.models import Order, OrderLineItem
from django.contrib.auth.decorators import login_required
import stripe,json
import traceback
from django.conf import settings

# Method below requires user to login
@login_required()
def payment_form(request):
    # If the request is a post request
    if request.method=="POST":
        cart = request.session.get('cart')
        # Calculate the total cost
        total = 0
        try:
            for id, quantity in cart.items():
                instrument = Instrument.objects.get(pk=id)
                total += quantity * instrument.cost
        except:
            print("Issue calculating the total")
            return render (request, 'index')
        # Create an order
        try:
            order = Order()
            order.totalCost = total
            order.delivery_street = request.POST.get('addressOne')
            order.delivery_town = request.POST.get('addressTwo')
            order.delivery_county = request.POST.get('addressThree')
            order.delivery_postcode = request.POST.get('postCode')
            order.customer_phone = request.POST.get('phone')
            order.customer = CustomUser.objects.get(email = request.user)
            order.save()
            # For each instrument that was in the cart create an order line item and remove the stock amount from the database
            for id, quantity in cart.items():
                instrument = Instrument.objects.get(pk = id)
                order_line = OrderLineItem()
                order_line.instrument = instrument
                order_line.quantity = quantity
                order_line.order = order
                order_line.save()
                instrument.stock_amount -= quantity
                instrument.save()
                # empty the cart
                request.session['cart'] = {}
            messages.info(request, "Your order has been successfully placed") 
        except:
            messages.info(request, "Theres was an issue creating the order details")  
            print(traceback.format_exc())
        return redirect ('instrument:view_instruments')

        #print("Post")
    # If the request is a get request, display forms required for payment
    return render(request, "payment.html")
    
    # Method to invoke Stripe API
def create_payment_intent(request):
    #Get the total cost of the cart contents
    total = 0
    try:
        cart = request.session.get('cart')
        for id, quantity in cart.items():
            instrument = Instrument.objects.get(pk=id)
            total += quantity * instrument.cost
    except:
        messages.info(request, "Theres was an issue retrieving the cart total cost")
        return render(request, "cart.html")
    # Try to create a payment intent using the stripe API
    try:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        intent = stripe.PaymentIntent.create(amount = int(total*100), currency = "eur", payment_method_types = ['card'],)
        # Retrieve the client secret key from the payment intent instance
        return JsonResponse({'client_secret': intent.client_secret})
    except:
        messages.info(request, "Theres was an issue connecting with Stripe")
        return render(request, "cart.html")
        
def payment_fail(request):
    # Display a message showing the payment has failed
    messages.info(request, "Payment Failed, Payments require a HTTPS connection")
    return render(request, "cart.html")
    

