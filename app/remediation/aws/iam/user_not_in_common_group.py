import boto3


def apply(user_name,
          common_group,
          access_key=None,
          secret_key=None,
          region=None):
    iam_client = boto3.client('iam',
                              region_name=region,
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key)
    response = iam_client.add_user_to_group(UserName=user_name,
                                            GroupName=common_group)
    return response


if __name__ == '__main__':
    print(apply('secops-test', 's3access'))
