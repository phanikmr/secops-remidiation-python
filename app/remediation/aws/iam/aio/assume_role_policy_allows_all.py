import json

import aioboto3


async def apply(role_name,
                principal,
                access_key=None,
                secret_key=None,
                region=None):
    session = aioboto3.Session()
    async with session.resource('iam',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region) as iam_client:
        assume_role = await iam_client.AssumeRolePolicy(role_name)
        role = await assume_role.Role()
        assume_role_policy_doc = await role.assume_role_policy_document
        for statement in assume_role_policy_doc['Statement']:
            statement['Principal'] = {'AWS': principal}
        response = await assume_role.update(
            PolicyDocument=json.dumps(assume_role_policy_doc))
        return response


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    print(
        loop.run_until_complete(
            apply('secops-test', 'phani', region='us-east-1')))
