import aioboto3


async def apply(bucket_name, access_key=None, secret_key=None, region=None):
    async with aioboto3.Session().resource('s3',
                                           aws_access_key_id=access_key,
                                           aws_secret_access_key=secret_key,
                                           region_name=region) as s3_bucket:
        bucket_versioning = await s3_bucket.BucketVersioning(bucket_name)
        response = await bucket_versioning.enable()
        return response
