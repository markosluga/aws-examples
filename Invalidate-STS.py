import boto3

def invalidate_sts_token(token):
    sts_client = boto3.client('sts')
    sts_client.invalidate_token(TokenId=token)
    print(f'Token {token} has been invalidated.')
