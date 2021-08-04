import boto3


def apply(access_key=None, secret_key=None, region=None):
    ec2_client = boto3.client('ec2',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    response = ec2_client.enable_ebs_encryption_by_default()
    return response


if __name__ == '__main__':
    print(apply(region='us-east-1'))
