import boto3


def apply(bucket_name, access_key=None, secret_key=None, region=None):
    s3_bucket = boto3.resource('s3',
                               aws_access_key_id=access_key,
                               aws_secret_access_key=secret_key,
                               region_name=region)
    bucket_versioning = s3_bucket.BucketVersioning(bucket_name)
    response = bucket_versioning.enable()
    return response


if __name__ == '__main__':
    print(apply('pot-nimo-config', region='us-east-1'))
