import boto3

def get_cognito_token(username, password):
    cognito_client = boto3.client('cognito-idp')

    # Get the user pool ID and client ID from the environment variables
    user_pool_id = os.environ['COGNITO_USER_POOL_ID']
    client_id = os.environ['COGNITO_CLIENT_ID']

    # Call the Cognito API to get an access token
    response = cognito_client.initiate_auth(
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password
        },
        ClientId=client_id,
        UserPoolId=user_pool_id
    )
    access_token = response['AuthenticationResult']['AccessToken']

    return access_token
