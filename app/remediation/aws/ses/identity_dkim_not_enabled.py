import boto3


def apply(identity, access_key=None, secret_key=None, region=None):
    ses_client = boto3.client('ses',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    response = ses_client.set_identity_dkim_enabled(Identity=identity,
                                                    DkimEnabled=True)
    return response
