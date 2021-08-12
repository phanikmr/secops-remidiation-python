import json

import aioboto3


async def apply(identity,
                policy_name,
                policy_doc,
                access_key=None,
                secret_key=None,
                region=None):
    async with aioboto3.Session().client('sqs',
                                         aws_access_key_id=access_key,
                                         aws_secret_access_key=secret_key,
                                         region_name=region) as sqs_client:
        response = await sqs_client.put_identity_policy(
            Identity=identity,
            PolicyName=policy_name,
            Policy=json.dumps(policy_doc))
    return response
