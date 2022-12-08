import boto3

def check_cognito_token(token):
    cognito_client = boto3.client('cognito-idp')

    # Get the user pool ID from the environment variable
    user_pool_id = os.environ['COGNITO_USER_POOL_ID']

    # Call the Cognito API to get the token information
    response = cognito_client.get_user(
        AccessToken=token,
        UserPoolId=user_pool_id
    )
    username = response['Username']

    # Check if the token is still valid
    now = datetime.datetime.now()
    token_expires = response['UserAttributes']['exp']['Value']
    token_expires = datetime.datetime.fromtimestamp(int(token_expires))
    if token_expires > now:
        print(f'Token for user {username} is valid.')
    else:
        print(f'Token for user {username} has expired.')
