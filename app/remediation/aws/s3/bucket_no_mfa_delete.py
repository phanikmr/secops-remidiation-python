import boto3


def apply(bucket_name,
          device_serial_number,
          auth_code,
          bucket_owner_account_id=None,
          access_key=None,
          secret_key=None,
          region=None):
    '''
    https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html
    '''
    s3_bucket = boto3.resource('s3',
                               aws_access_key_id=access_key,
                               aws_secret_access_key=secret_key,
                               region_name=region)
    bucket_versioning = s3_bucket.BucketVersioning(bucket_name)
    if bucket_owner_account_id:
        return bucket_versioning.enable(
            MFA=device_serial_number + ' ' + auth_code,
            ExpectedBucketOwner=bucket_owner_account_id)
    return bucket_versioning.enable(MFA=device_serial_number + ' ' + auth_code)
