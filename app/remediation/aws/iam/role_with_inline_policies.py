import boto3


def apply(role_name,
          policy_name,
          access_key=None,
          secret_key=None,
          region=None):
    iam_client = boto3.client('iam',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    response = iam_client.delete_role_policy(RoleName=role_name,
                                             PolicyName=policy_name)
    return response
