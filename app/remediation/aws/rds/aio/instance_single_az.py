import aioboto3


async def apply(db_instance_id, access_key=None, secret_key=None, region=None):
    session = aioboto3.Session()
    async with session.client('rds',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region) as rds_client:
        response = await rds_client.modify_db_instance(
            DBInstanceIdentifier=db_instance_id, MultiAZ=True)
        return response


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(apply(''))
