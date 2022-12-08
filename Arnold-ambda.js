import boto3

def invalidate_sts_token(token):
    sts_client = boto3.client('sts')
    sts_client.invalidate_token(TokenId=token)
    print(f'Token {token} has been invalidated.')

def extract_identity_and_token(log_entry):
    identity = log_entry['userIdentity']
    token_id = identity['sessionContext']['sessionToken']
    caller = identity['arn']
    print(f'Identity: {caller}')
    print(f'Token ID: {token_id}')

    # Access DynamoDB and retrieve the item with the caller's identity
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('my-table')
    response = table.get_item(Key={'identity': caller})
    item = response.get('Item')

    # Check if the item exists and print a message
    if item:
        print(f'Identity {caller} is registered in the table.')
    else:
        print(f'Identity {caller} is not registered in the table.')
        # Invalidate the STS token
        invalidate_sts_token(token_id)
