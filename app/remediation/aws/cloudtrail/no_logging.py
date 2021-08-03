import boto3


def apply(trail_name,
          enable_s3_events=True,
          enable_lambda_events=True,
          enable_dynamodb_events=True,
          access_key=None,
          secret_key=None,
          region=None):
    cloudtrail_client = boto3.client('cloudtrail',
                                     aws_access_key_id=access_key,
                                     aws_secret_access_key=secret_key,
                                     region_name=region)
    data_resources = []
    if enable_s3_events:
        data_resources.append({
            'Type': 'AWS::S3::Object',
            'Values': ['arn:aws:s3:::']
        })
    if enable_lambda_events:
        data_resources.append({
            'Type': 'AWS::Lambda::Function',
            'Values': ['arn:aws:lambda']
        })
    if enable_dynamodb_events:
        data_resources.append({
            'Type': 'AWS::DynamoDB::Table',
            'Values': ['arn:aws:dynamodb']
        })
    response = cloudtrail_client.put_event_selectors(
        TrailName=trail_name,
        EventSelectors=[{
            'ReadWriteType': 'All',
            'IncludeManagementEvents': True,
            'DataResources': data_resources
        }])
    return response


if __name__ == '__main__':
    print(apply(trail_name='test-trail', region='ap-south-1'))
