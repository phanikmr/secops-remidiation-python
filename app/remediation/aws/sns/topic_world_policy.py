import boto3


def apply(topic_arn,
          statement_name,
          account_ids,
          actions,
          statement_to_delete_name=None,
          access_key=None,
          secret_key=None,
          region=None):
    sns_client = boto3.client('sns',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    if statement_to_delete_name:
        sns_client.remove_permission(TopicArn=topic_arn,
                                     Label=statement_to_delete_name)
    response = sns_client.add_permission(TopicArn=topic_arn,
                                         Label=statement_name,
                                         AWSAccountId=account_ids,
                                         ActionName=actions)
    return response


if __name__ == '__main__':
    print(
        apply(
            'arn:aws:sns:us-east-1:426811776660:DescribeAndDeleteEBSSnapshotSNSTopic',
            'test_policy_sns', ['426811776660'], ['Publish'],
            '__default_statement_ID'))
