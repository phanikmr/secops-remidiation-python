import boto3


def apply(load_balancer_name,
          s3_bucket_name,
          s3_prefix='',
          emit_interval=60,
          access_key=None,
          secret_key=None,
          region=None):
    elb_client = boto3.client('elb',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    response = elb_client.modify_load_balancer_attributes(
        LoadBalancerName=load_balancer_name,
        LoadBalancerAttributes={
            'AccessLog': {
                'Enabled': True,
                'S3BucketName': s3_bucket_name,
                'EmitInterval': emit_interval,
                'S3BucketPrefix': s3_prefix
            }
        })
    return response
