import boto3

def invalidate_sts_token(token):
    sts_client = boto3.client('sts')
    sts_client.invalidate_token(TokenId=token)
    print(f'Token {token} has been invalidated.')

def apply_deny_all_policy(username):
    iam_client = boto3.client('iam')
    policy_name = 'DenyAllAccess'
    policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "DenyAll",
                "Effect": "Deny",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }

    # Create the policy
    response = iam_client.create_policy(
        PolicyName=policy_name,
        PolicyDocument=json.dumps(policy_document)
    )
    policy_arn = response['Policy']['Arn']

    # Attach the policy to the user
    iam_client.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )
    print(f'Policy {policy_name} has been attached to user {username}.')

