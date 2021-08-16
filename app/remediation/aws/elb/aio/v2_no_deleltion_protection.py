import aioboto3


async def apply(load_balancer_arn,
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
                'Key': 'deletion_protection.enabled',
                'Value': 'true'
            }])
        return response
