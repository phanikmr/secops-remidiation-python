import boto3

from .root_account_no_mfa import apply as enable_mfa


def apply(user_name,
          permission_boundary=None,
          policy_arn=None,
          access_key=None,
          secret_key=None,
          region=None):
    iam_client = boto3.client('iam',
                              region_name=region,
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key)
    if permission_boundary:
        user = iam_client.create_user(UserName=user_name,
                                      PermissionsBoundary=permission_boundary)
    else:
        user = iam_client.create_user(UserName=user_name)
    enable_mfa(user_name=user_name,
               access_key=access_key,
               secret_key=secret_key,
               region=region)
    if policy_arn:
        if isinstance(policy_arn, str):
            iam_client.attach_user_policy(UserName=user_name,
                                          PolicyArn=policy_arn)
        elif isinstance(policy_arn, list):
            for policy in policy_arn:
                iam_client.attach_user_policy(UserName=user_name,
                                              PolicyArn=policy)
    return user


if __name__ == '__main__':
    print(apply('secops-test'))
