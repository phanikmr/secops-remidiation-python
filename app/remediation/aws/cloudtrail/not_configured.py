import json

import boto3


def apply(trail_name,
          bucket_name,
          s3_key_prefix='',
          create_bucket=False,
          access_key=None,
          secret_key=None,
          region=None):
    '''Creates bucket & cloudtrail'''
    cloudtrail_client = boto3.client('cloudtrail',
                                     aws_access_key_id=access_key,
                                     aws_secret_access_key=secret_key,
                                     region_name=region)
    if create_bucket:
        s3_client = boto3.client('s3',
                                 aws_access_key_id=access_key,
                                 aws_secret_access_key=secret_key,
                                 region_name=region)
        s3_client.create_bucket(
            ACL='private',
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region})
        policy = {
            'Version':
                '2012-10-17',
            'Statement': [{
                'Sid': 'AWSCloudTrailAclCheck20150319',
                'Effect': 'Allow',
                'Principal': {
                    'Service': 'cloudtrail.amazonaws.com'
                },
                'Action': 's3:GetBucketAcl',
                'Resource': 'arn:aws:s3:::' + bucket_name
            }, {
                'Sid':
                    'AWSCloudTrailWrite20150319',
                'Effect':
                    'Allow',
                'Principal': {
                    'Service': 'cloudtrail.amazonaws.com'
                },
                'Action':
                    's3:PutObject',
                'Resource':
                    'arn:aws:s3:::' + bucket_name +
                    ('/' + s3_key_prefix if s3_key_prefix else '') + '/*',
                'Condition': {
                    'StringEquals': {
                        's3:x-amz-acl': 'bucket-owner-full-control'
                    }
                }
            }]
        }
        s3_client.put_bucket_policy(Bucket=bucket_name,
                                    Policy=json.dumps(policy))

    response = cloudtrail_client.create_trail(Name=trail_name,
                                              S3BucketName=bucket_name,
                                              S3KeyPrefix=s3_key_prefix,
                                              IsMultiRegionTrail=True,
                                              EnableLogFileValidation=True,
                                              TagsList=[{
                                                  'Key': 'creator',
                                                  'Value': 'Spot Security'
                                              }])
    response = cloudtrail_client.start_logging(Name=response['TrailARN'])
    return response
