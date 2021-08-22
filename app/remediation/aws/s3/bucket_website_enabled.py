import boto3


def apply(bucket_name,
          bucket_owner_id=None,
          access_key=None,
          secret_key=None,
          region=None):
    s3_client = boto3.client('s3',
                             aws_access_key_id=access_key,
                             aws_secret_access_key=secret_key,
                             region_name=region)
    if bucket_owner_id:
        return s3_client.delete_bucket_website(
            Bucket=bucket_name, ExpectedBucketOwner=bucket_owner_id)
    return s3_client.delete_bucket_website(Bucket=bucket_name)
