import json

import boto3


def apply(identity,
          policy_name,
          policy_doc,
          access_key=None,
          secret_key=None,
          region=None):
    ses_client = boto3.client('ses',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    response = ses_client.put_identity_policy(Identity=identity,
                                              PolicyName=policy_name,
                                              Policy=json.dumps(policy_doc))
    return response
