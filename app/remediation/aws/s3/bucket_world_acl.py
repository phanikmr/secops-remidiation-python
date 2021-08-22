import boto3


def apply(bucket_name, access_key=None, secret_key=None, region=None):
    s3_client = boto3.client('s3',
                             aws_access_key_id=access_key,
                             aws_secret_access_key=secret_key,
                             region_name=region)
    return s3_client.put_bucket_acl(Bucket=bucket_name, ACL='private')
