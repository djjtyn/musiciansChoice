from django.shortcuts import render
import boto3
from django.contrib import messages
import traceback

# Create your views here.
def notify_when_product_is_back_in_stock(request, instrument_id):
    # Create a topic if it doesn't exist already, if it does exist get the topics ARN
    try:
        sns_client = boto3.client('sns')
        response = sns_client.create_topic(Name="test")
        print(response["TopicArn"])
    except:
         print(traceback.format_exc())
    # topic_arn = response['TokenArn']
    # print(topic_arn)
    # userEmail = request.user
    # print(userEmail)
    # print(f"Subscribing to topic {topic_arn}")
    # try:
    #     subscription = sns_client.subscribe(TopicArn=topic_arn, Protocol='email', Endpoint = request.user, ReturnSubscriptionArn = True)
    #     print(subscription)
    #     messages.info(request, f"{request.user} wil rceive an email when this product is back in stock")
    # except:
    #     messages.info(request, "An error occured processing this request")
    return render (request, "index.html")
