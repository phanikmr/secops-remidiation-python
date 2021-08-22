import boto3


def apply(bucket_name,
          target_bucket_name,
          prefix=None,
          access_key=None,
          secret_key=None,
          region=None):
    s3_bucket = boto3.resource('s3',
                               aws_access_key_id=access_key,
                               aws_secret_access_key=secret_key,
                               region_name=region)
    bucket_logging = s3_bucket.BucketLogging(bucket_name)
    response = bucket_logging.put(
        BucketLoggingStatus={
            'LoggingEnabled': {
                'TargetBucket': target_bucket_name,
                'TargetPrefix': prefix if prefix else f'{bucket_name}/'
            }
        })
    return response


if __name__ == '__main__':
    print(apply('pot-nimo-config', 'pmamta-ops', region='us-east-1'))
