import boto3


def apply(subnet_id, bucket_arn, access_key=None, secret_key=None, region=None):
    vpc_client = boto3.client('ec2',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    response = vpc_client.create_flow_logs(
        ResourceIds=[subnet_id],
        ResourceType=['Subnet'],
        TrafficType='ALL',
        LogDestinationType='s3',
        LogDestination=bucket_arn,
    )
    return response
