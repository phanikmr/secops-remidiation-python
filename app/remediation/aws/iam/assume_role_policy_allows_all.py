import json

import boto3


def apply(role_name, principal, access_key=None, secret_key=None, region=None):
    iam_client = boto3.resource('iam',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)
    assume_role = iam_client.AssumeRolePolicy(role_name)
    role = assume_role.Role()
    assume_role_policy_doc = role.assume_role_policy_document
    for statement in assume_role_policy_doc['Statement']:
        statement['Principal'] = {'AWS': principal}
    response = assume_role.update(
        PolicyDocument=json.dumps(assume_role_policy_doc))
    return response


if __name__ == '__main__':
    print(apply('secops-test', 'phani', region='us-east-1'))
    