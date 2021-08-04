import aioboto3


async def apply(access_key=None, secret_key=None, region=None):
    session = aioboto3.Session()
    async with session.client('ec2',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region) as ec2_client:
        response = await ec2_client.enable_ebs_encryption_by_default()
        return response


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(apply(region='us-east-1')))
