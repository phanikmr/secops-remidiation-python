import boto3


def apply(doamin, access_key=None, secret_key=None, region=None):
    route53_client = boto3.client('route53domains',
                                  aws_access_key_id=access_key,
                                  aws_secret_access_key=secret_key,
                                  region_name=region)
    response = route53_client.enable_domain_auto_renew(DomainName=doamin)
    return response
