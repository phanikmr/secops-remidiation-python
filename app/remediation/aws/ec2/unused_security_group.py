import boto3


def apply(security_group_id, access_key=None, secret_key=None, region=None):
    ec2_client = boto3.client('ec2',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    response = ec2_client.delete_security_group(GroupId=security_group_id)
    return response
