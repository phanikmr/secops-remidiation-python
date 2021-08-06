import json

import aioboto3


async def apply(role_name,
                policy_name,
                new_actions,
                access_key=None,
                secret_key=None,
                region=None):
    session = aioboto3.Session()
    async with session.resource('iam',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region) as iam_client:
        role_policy = await iam_client.RolePolicy(role_name, policy_name)
        policy_doc = await role_policy.policy_document
        for statement in policy_doc['Statement']:
            if 'Effect' in statement and statement[
                    'Effect'] == 'Allow' and 'NotAction' in statement:
                del statement['NotAction']
                statement['Action'] = new_actions
        await role_policy.delete()
        response = await role_policy.put(PolicyDocument=json.dumps(policy_doc))
        return response


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    print(
        loop.run_until_complete(
            apply('secops-test',
                  's3-policy-secops-test', ['s3:Get*', 's3:List*'],
                  region='us-east-1')))
