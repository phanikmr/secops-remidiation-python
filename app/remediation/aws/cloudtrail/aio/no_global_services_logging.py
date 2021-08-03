import aioboto3


async def apply(trail_name, access_key=None, secret_key=None, region=None):
    session = aioboto3.Session()
    async with session.client('cloudtrail',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region) as cloudtrail_client:
        response = await cloudtrail_client.update_trail(Name=trail_name,
                                                        IsMultiRegionTrail=True)
        return response
