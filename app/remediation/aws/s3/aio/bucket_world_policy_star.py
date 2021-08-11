import json

import aioboto3


async def apply(bucket_name,
                policy_doc,
                account_id=None,
                access_key=None,
                secret_key=None,
                region=None):
    async with aioboto3.Session().client('s3',
                                         aws_access_key_id=access_key,
                                         aws_secret_access_key=secret_key,
                                         region_name=region) as s3_client:
        if not account_id:
            async with aioboto3.Session().client(
                    'sts',
                    aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key,
                    region_name=region) as sts_client:
                account_id = await sts_client.get_caller_identity()
                account_id = account_id['Account']
        response = await s3_client.put_bucket_policy(
            Bucket=bucket_name,
            ConfirmRemoveSelfBucketAccess=True,
            Policy=json.dumps(policy_doc),
            ExpectedBucketOwner=account_id)
    return response
