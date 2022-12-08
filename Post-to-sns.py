import boto3

def send_message_to_topic(topic_arn, message):
    sns_client = boto3.client('sns')

    # Publish the message to the specified topic
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=message
    )
    message_id = response['MessageId']

    print(f'Message {message_id} was sent to topic {topic_arn}.')
