import json

import aioboto3


async def apply(policy_arn,
                new_actions,
                access_key=None,
                secret_key=None,
                region=None):
    session = aioboto3.Session()
    async with session.client('iam',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region) as iam_client:
        policy = await iam_client.get_policy(PolicyArn=policy_arn)
        default_policy = await iam_client.get_policy_version(
            PolicyArn=policy_arn,
            VersionId=policy['Policy']['DefaultVersionId'])
        prev_version_id = policy['Policy']['DefaultVersionId']
        for statement in default_policy['PolicyVersion']['Document'][
                'Statement']:
            statement['Action'] = new_actions

        response = await iam_client.create_policy_version(
            PolicyArn=policy_arn,
            PolicyDocument=json.dumps(
                default_policy['PolicyVersion']['Document']),
            SetAsDefault=True)
        await iam_client.delete_policy_version(PolicyArn=policy_arn,
                                               VersionId=prev_version_id)
    return response


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    print(
        loop.run_until_complete(
            apply('arn:aws:iam::426811776660:policy/secops-test',
                  ['s3:Get*', 's3:List*'],
                  region='us-east-1')))
                  