import aioboto3


async def apply(bucket_name,
                target_bucket_name,
                prefix=None,
                access_key=None,
                secret_key=None,
                region=None):
    async with aioboto3.Session().resource('s3',
                                           aws_access_key_id=access_key,
                                           aws_secret_access_key=secret_key,
                                           region_name=region) as s3_bucket:
        bucket_logging = await s3_bucket.BucketLogging(bucket_name)
        response = await bucket_logging.put(
            BucketLoggingStatus={
                'LoggingEnabled': {
                    'TargetBucket': target_bucket_name,
                    'TargetPrefix': prefix if prefix else f'{bucket_name}/'
                }
            })
        return response


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    print(
        loop.run_until_complete(
            apply('pot-nimo-config', 'pmamta-ops', region='us-east-1')))
