import aioboto3


async def apply(cluster_id, access_key=None, secret_key=None, region=None):
    session = aioboto3.Session()
    async with session.client('redshift',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region) as redshift_client:
        response = await redshift_client.modify_db_instance(
            ClusterIdentifier=cluster_id, AllowVersionUpgrade=True)
        return response
