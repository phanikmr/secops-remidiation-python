import pprint

import boto3


def apply(user_name, access_key=None, secret_key=None, region=None):
    iam_client = boto3.client('iam',
                              region_name=region,
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key)
    keys = iam_client.list_access_keys(UserName=user_name)
    new_key = iam_client.create_access_key(UserName=user_name)
    pprint.pprint(new_key)
    print('Save the keys. Will ne shown only once')
    for key in keys['AccessKeyMetadata']:
        iam_client.delete_access_key(UserName=user_name,
                                     AccessKeyId=key['AccessKeyId'])
    return new_key


if __name__ == '__main__':
    print(apply('secops-test'))
