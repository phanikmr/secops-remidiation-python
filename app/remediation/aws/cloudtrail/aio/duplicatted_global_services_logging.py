import aioboto3


async def apply(duplicate_trail_name,
                stop_logging=False,
                access_key=None,
                secret_key=None,
                region=None):
    async with aioboto3.Session().client(
            'cloudtrail',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region) as cloudtrail_client:
        response = await cloudtrail_client.update_trail(
            Name=duplicate_trail_name, IsMultiRegionTrail=False)
        if stop_logging:
            await cloudtrail_client.stop_logging(Name=duplicate_trail_name)
        return response
