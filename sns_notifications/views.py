from django.shortcuts import render, redirect
import boto3
from django.contrib import messages
import traceback
from django.contrib.auth.decorators import login_required
from .sns_utils import sns

# Login required to be notified on stock return for products
@login_required()
def notify_when_product_is_back_in_stock(request, instrument_id):
    # Create a topic if it doesn't exist already, if it does exist get the topics ARN
    try:
        user_email = request.user.email
        sns.topic_subscribe(f"restockNotificationForInstrumentId{instrument_id}", user_email)
        messages.info(request, f"An email was sent to {user_email} to confirm signing up to receive a notification when this product is back in stock")
    except:
        messages.info(request, "An error occured processing this request")
        print(traceback.format_exc())
    return redirect ('instrument:view_instruments')
