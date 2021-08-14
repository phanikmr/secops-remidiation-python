import json

import boto3


def apply(endpoint_id,
          policy_doc,
          access_key=None,
          secret_key=None,
          region=None):
    vpc_client = boto3.client('ec2',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    response = vpc_client.modify_vpc_endpoint(
        VpcEndpointId=endpoint_id, PolicyDocument=json.dumps(policy_doc))
    return response
