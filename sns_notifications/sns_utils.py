import boto3
from botocore.exceptions import ClientError
import logging

class sns:
    
    @staticmethod
    def create_topic(topic_name):
        try:
            sns_client = boto3.client('sns')
            response = sns_client.create_topic(Name=topic_name)
            return response['TopicArn']
        except ClientError as e:
            logging.error(e)
            print("An isue occured creating the topic")
            
        
    @staticmethod
    def topic_subscribe(topic_name, user_email):
        try:
            sns_client = boto3.client('sns')
            response = sns_client.create_topic(Name=topic_name)
            topic_arn = response['TopicArn']
            print("Subscribing")
            sns_client.subscribe(TopicArn=topic_arn, Protocol = 'email', Endpoint = user_email)
        except ClientError as e:
            logging.error(e)
            print("An isue occured subscribing")
            
    @staticmethod
    def publish_to_topic_and_remove_topic(topic_name, message):
        sns_client = boto3.client('sns')
        try:
            # Try to publish the message
            response = sns_client.create_topic(Name = topic_name)
            topic_arn = response['TopicArn']
            response = sns_client.publish(TopicArn = topic_arn, Message = message)
            # Try to delete the topic
            try:
                response = sns_client.delete_topic(TopicArn = topic_arn)
            except ClientError as e:
                logging.error(e)
                print("An isue occured publishing the message")
        except ClientError as e:
            logging.error(e)
            print("An isue occured in the message publish process")
            
            
        
    