import aioboto3


async def apply(cluster_id,
                kms_id,
                access_key=None,
                secret_key=None,
                region=None):
    async with aioboto3.Session().client('redshift',
                                         aws_access_key_id=access_key,
                                         aws_secret_access_key=secret_key,
                                         region_name=region) as redshift_client:
        response = await redshift_client.modify_cluster(
            ClusterIdentifier=cluster_id, Encrypted=True, KmsKeyId=kms_id)
        return response
