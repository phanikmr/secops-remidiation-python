import aioboto3


async def apply(alarm_name: str,
                ok_actions: list,
                insufficient_data_actions: list,
                alarm_actions: list,
                access_key=None,
                secret_key=None,
                region=None):
    '''\
    For alarm actions Ref:
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_alarm
    '''
    session = aioboto3.Session()
    async with session.client('cloudwatch',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region) as cloudwatch_client:
        response = await cloudwatch_client.put_metric_alarm(
            AlarmName=alarm_name,
            ActionsEnabled=True,
            OKActions=ok_actions,
            AlarmActions=alarm_actions,
            InsufficientDataActions=insufficient_data_actions)
        return response
