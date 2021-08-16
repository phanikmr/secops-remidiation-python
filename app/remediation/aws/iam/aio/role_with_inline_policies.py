import aioboto3


async def apply(role_name,
                policy_name,
                access_key=None,
                secret_key=None,
                region=None):
    session = aioboto3.Session()
    async with session.client('iam',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region) as iam_client:
        response = await iam_client.delete_role_policy(RoleName=role_name,
                                                       PolicyName=policy_name)
        return response
