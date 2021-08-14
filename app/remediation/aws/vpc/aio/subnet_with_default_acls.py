import aioboto3


async def apply(ipv4_cidr_block, access_key=None, secret_key=None, region=None):
    async with aioboto3.Session().client('ec2',
                                         aws_access_key_id=access_key,
                                         aws_secret_access_key=secret_key,
                                         region_name=region) as vpc_client:
        response = await vpc_client.create_vpc(CidrBlock=ipv4_cidr_block)
    return response
