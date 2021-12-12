from django.shortcuts import render, redirect
import boto3
from django.contrib import messages
import traceback
from django.contrib.auth.decorators import login_required

# Login required to be notified on stock return for products
@login_required()
def notify_when_product_is_back_in_stock(request, instrument_id):
    # Create a topic if it doesn't exist already, if it does exist get the topics ARN
    try:
        sns_client = boto3.client('sns')
        response = sns_client.create_topic(Name=f"stockNotificationForInstrumentid{instrument_id}")
        topic_arn = response['TokenArn']
        userEmail = request.user
        subscription = sns_client.subscribe(TopicArn=topic_arn, Protocol='email', Endpoint = request.user, ReturnSubscriptionArn = True)
        messages.info(request, f"{userEmail} will be notified when stock returns")
    except:
        messages.info(request, "An error occured processing this request")
        print(traceback.format_exc())
    return redirect ('instrument:view_instruments')
