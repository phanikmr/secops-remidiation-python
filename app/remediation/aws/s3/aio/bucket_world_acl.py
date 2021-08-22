import aioboto3


async def apply(bucket_name, access_key=None, secret_key=None, region=None):
    async with aioboto3.Session().client('s3',
                                         aws_access_key_id=access_key,
                                         aws_secret_access_key=secret_key,
                                         region_name=region) as s3_client:
        return await s3_client.put_bucket_acl(Bucket=bucket_name, ACL='private')
