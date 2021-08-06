import json

import boto3


def apply(policy_arn,
          new_actions,
          access_key=None,
          secret_key=None,
          region=None):
    iam_client = boto3.resource('iam',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)
    policy = iam_client.Policy(policy_arn)
    default_policy = policy.default_version
    prev_version_id = default_policy.version_id
    for statement in default_policy.document['Statement']:
        if 'Effect' in statement and statement[
                'Effect'] == 'Allow' and 'NotAction' in statement:
            del statement['NotAction']
            statement['Action'] = new_actions

    response = policy.create_version(PolicyDocument=json.dumps(
        default_policy.document),
                                     SetAsDefault=True)
    boto3.client('iam',
                 aws_access_key_id=access_key,
                 aws_secret_access_key=secret_key,
                 region_name=region).delete_policy_version(
                     PolicyArn=policy_arn, VersionId=prev_version_id)
    return response


if __name__ == '__main__':
    print(
        apply('arn:aws:iam::426811776660:policy/secops-test',
              ['s3:Get*', 's3:List*'],
              region='us-east-1'))
