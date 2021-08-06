import json

import boto3


def apply(role_name,
          policy_name,
          new_actions,
          access_key=None,
          secret_key=None,
          region=None):
    iam_client = boto3.resource('iam',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)
    role_policy = iam_client.RolePolicy(role_name, policy_name)
    policy_doc = role_policy.policy_document
    for statement in policy_doc['Statement']:
        if 'Effect' in statement and statement[
                'Effect'] == 'Allow' and 'NotAction' in statement:
            del statement['NotAction']
            statement['Action'] = new_actions
    role_policy.delete()
    response = role_policy.put(PolicyDocument=json.dumps(policy_doc))
    return response


if __name__ == '__main__':
    print(
        apply('secops-test',
              's3-policy-secops-test', ['s3:Get*', 's3:List*'],
              region='us-east-1'))
