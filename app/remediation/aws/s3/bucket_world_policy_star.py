import json

import boto3


def apply(bucket_name,
          policy_doc,
          account_id=None,
          access_key=None,
          secret_key=None,
          region=None):
    s3_client = boto3.client('s3',
                             aws_access_key_id=access_key,
                             aws_secret_access_key=secret_key,
                             region_name=region)
    account_id = account_id if account_id else boto3.client(
        'sts',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region).get_caller_identity()['Account']
    response = s3_client.put_bucket_policy(Bucket=bucket_name,
                                           ConfirmRemoveSelfBucketAccess=True,
                                           Policy=json.dumps(policy_doc),
                                           ExpectedBucketOwner=account_id)
    return response
