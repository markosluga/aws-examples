def extract_identity_and_token(log_entry):
    identity = log_entry['userIdentity']
    token_id = identity['sessionContext']['sessionToken']
    caller = identity['arn']
    print(f'Identity: {caller}')
    print(f'Token ID: {token_id}')
