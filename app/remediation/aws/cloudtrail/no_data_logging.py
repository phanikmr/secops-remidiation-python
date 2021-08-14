import boto3


def apply(trail_name,
          target_bucket_name,
          s3_key_prefix='',
          access_key=None,
          secret_key=None,
          region=None):
    cloudtrail_client = boto3.client('cloudtrail',
                                     aws_access_key_id=access_key,
                                     aws_secret_access_key=secret_key,
                                     region_name=region)
    trail = cloudtrail_client.get_trail(Name=trail_name)
    bucket_name = trail['Trail']['S3BucketName']
    s3_client = boto3.client('s3',
                             aws_access_key_id=access_key,
                             aws_secret_access_key=secret_key,
                             region_name=region)
    s3_client.put_bucket_acl(
        Bucket=target_bucket_name,
        GrantWrite='URI=http://acs.amazonaws.com/groups/s3/LogDelivery',
        GrantReadACP='URI=http://acs.amazonaws.com/groups/s3/LogDelivery ')
    response = s3_client.put_bucket_logging(
        Bucket=bucket_name,
        BucketLoggingStatus={
            'LoggingEnabled': {
                'TargetBucket': target_bucket_name,
                'TargetPrefix': s3_key_prefix
            }
        })
    return response


if __name__ == '__main__':
    print(
        apply('test-trail',
              region='ap-south-1',
              target_bucket_name='pmamta-ops'))
