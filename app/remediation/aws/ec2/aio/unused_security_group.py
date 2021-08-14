import aioboto3


async def apply(security_group_id,
                access_key=None,
                secret_key=None,
                region=None):
    session = aioboto3.Session()
    async with session.client('ec2',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region) as ec2_client:
        response = await ec2_client.delete_security_group(
            GroupId=security_group_id)
        return response
