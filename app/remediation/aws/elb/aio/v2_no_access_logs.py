import aioboto3


async def apply(load_balancer_arn,
                s3_bucket_name,
                s3_prefix='',
                access_key=None,
                secret_key=None,
                region=None):
    async with aioboto3.Session().client('elbv2',
                                         aws_access_key_id=access_key,
                                         aws_secret_access_key=secret_key,
                                         region_name=region) as elb_client:
        response = await elb_client.modify_load_balancer_attributes(
            LoadBalancerArn=load_balancer_arn,
            Attributes=[{
                'Key': 'access_logs.s3.enabled',
                'Value': 'true'
            }, {
                'Key': 'access_logs.s3.bucket',
                'Value': s3_bucket_name
            }, {
                'Key': 'access_logs.s3.prefix',
                'Value': s3_prefix
            }])
        return response
