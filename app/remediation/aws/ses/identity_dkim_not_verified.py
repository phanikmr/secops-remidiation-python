import boto3


def apply(domain, access_key=None, secret_key=None, region=None):
    ses_client = boto3.client('ses',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    response = ses_client.verify_domain_dkim(Domain=domain)
    return response
