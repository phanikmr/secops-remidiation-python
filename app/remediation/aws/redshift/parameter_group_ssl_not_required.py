import boto3


def apply(group_name, access_key=None, secret_key=None, region=None):
    redshift_client = boto3.client('redshift',
                                   aws_access_key_id=access_key,
                                   aws_secret_access_key=secret_key,
                                   region_name=region)
    response = redshift_client.modify_cluster_parameter_group(
        ParameterGroupName=group_name,
        Parameters=[{
            'ParameterName': 'require_ssl',
            'ParameterValue': 'true'
        }])
    return response
