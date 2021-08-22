import boto3


def apply(parameter_group_name, access_key=None, secret_key=None, region=None):
    redshift_client = boto3.client('redshift',
                                   aws_access_key_id=access_key,
                                   aws_secret_access_key=secret_key,
                                   region_name=region)
    response = redshift_client.modify_cluster_parameter_group(
        ParameterGroupName=parameter_group_name,
        Parameters=[
            {
                'ParameterName': 'enable_user_activity_logging',
                'ParameterValue': 'true'
            },
        ])
    return response


if __name__ == '__main__':
    print(apply('myclusterparametergroup', region='us-east-1'))
