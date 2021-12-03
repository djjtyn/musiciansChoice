from django.shortcuts import render
from django.http import JsonResponse
import stripe,json
import os
if os.path.exists("env.py"):
    import env as env_variables

# Create your views here.
def payment_form(request):
    # If the request is a post request, try to process the payment
    # if request.method=="POST":
    #     print (request.POST.get('cardholder_name'))
    #     print (request.POST.get('cardNumber'))
    #     print (request.POST.get('supplier'))
    #     print (request.POST.get('supplier'))
    #     print (request.POST.get('supplier'))
    #     print (request.POST.get('supplier'))
    #     print (request.POST.get('supplier'))
    #     print (request.POST.get('supplier'))
        #print("Post")
    # If the request is a get request, display forms required for payment
    return render(request, "payment.html")
    
    # Method to invoke Stripe API
def create_payment_intent(request):
    # Try to create a payment intent using the stripe API
    stripe.api_key = env_variables.get_stripe_secret()
    print("I have been called")
    intent = stripe.PaymentIntent.create(amount = 60, currency = "eur")
    # Retrieve the client secret key from the payment intent instance
    return JsonResponse({'client_secret': intent.client_secret})

