import boto3


def apply(account_id=None, access_key=None, secret_key=None, region=None):
    s3_client = boto3.client('s3control',
                             aws_access_key_id=access_key,
                             aws_secret_access_key=secret_key,
                             region_name=region)
    account_id = account_id if account_id else boto3.client(
        'sts',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region).get_caller_identity()['Account']
    response = s3_client.put_public_access_block(
        AccountId=account_id,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        })
    return response


if __name__ == '__main__':
    print(apply())
