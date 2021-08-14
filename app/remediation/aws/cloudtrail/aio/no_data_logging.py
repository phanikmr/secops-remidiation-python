import aioboto3


async def apply(trail_name,
                target_bucket_name,
                s3_key_prefix='',
                access_key=None,
                secret_key=None,
                region=None):
    async with aioboto3.Session().client(
            'cloudtrail',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region) as cloudtrail_client:
        trail = await cloudtrail_client.get_trail(Name=trail_name)
        bucket_name = trail['Trail']['S3BucketName']
        async with aioboto3.Session().client('s3',
                                             aws_access_key_id=access_key,
                                             aws_secret_access_key=secret_key,
                                             region_name=region) as s3_client:
            await s3_client.put_bucket_acl(
                Bucket=target_bucket_name,
                GrantWrite='URI=http://acs.amazonaws.com/groups/s3/LogDelivery',
                GrantReadACP=
                'URI=http://acs.amazonaws.com/groups/s3/LogDelivery ')
            response = await s3_client.put_bucket_logging(
                Bucket=bucket_name,
                BucketLoggingStatus={
                    'LoggingEnabled': {
                        'TargetBucket': target_bucket_name,
                        'TargetPrefix': s3_key_prefix
                    }
                })
            return response


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    print(
        loop.run_until_complete(
            apply('test-trail',
                  region='ap-south-1',
                  target_bucket_name='pmamta-ops')))
