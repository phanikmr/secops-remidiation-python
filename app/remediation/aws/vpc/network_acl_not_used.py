import boto3


def apply(network_acl_id, access_key=None, secret_key=None, region=None):
    vpc_client = boto3.client('ec2',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    response = vpc_client.delete_network_acl(NetworkAclId=network_acl_id)
    return response
