import boto3


def apply(listener_arn,
          ssl_policy,
          access_key=None,
          secret_key=None,
          region=None):
    elb_client = boto3.client('elbv2',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    response = elb_client.modify_listener(ListenerArn=listener_arn,
                                          SslPolicy=ssl_policy)
    return response
