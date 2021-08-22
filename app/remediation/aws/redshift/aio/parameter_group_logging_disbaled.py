import aioboto3


async def apply(parameter_group_name,
                access_key=None,
                secret_key=None,
                region=None):
    session = aioboto3.Session()
    async with session.client('iam',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region) as redshift_client:
        response = await redshift_client.modify_cluster_parameter_group(
            ParameterGroupName=parameter_group_name,
            Parameters=[
                {
                    'ParameterName': 'enable_user_activity_logging',
                    'ParameterValue': 'true'
                },
            ])
    return response
