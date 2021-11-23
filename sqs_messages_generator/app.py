import boto3
import os

sqs = boto3.resource('sqs')
QUEUE = os.environ['QUEUE']
MESSAGE_COUNT = os.environ['MESSAGE_COUNT']

def lambda_handler(event, context):
    # Retrieving a queue by its name
    queue = sqs.get_queue_by_name(QueueName=QUEUE)

    # Create a new message
    response = queue.send_message(MessageBody='test message with ' + MESSAGE_COUNT)

    # The response is not a resource, but gives you a message ID and MD5
    print("MessageId created: {0}".format(response.get('MessageId')))
    print("MD5 created: {0}".format(response.get('MD5OfMessageBody')))
