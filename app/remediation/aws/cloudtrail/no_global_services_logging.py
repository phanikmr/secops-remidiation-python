import boto3


def apply(trail_name, access_key=None, secret_key=None, region=None):
    cloudtrail_client = boto3.client('cloudtrail',
                                     aws_access_key_id=access_key,
                                     aws_secret_access_key=secret_key,
                                     region_name=region)
    response = cloudtrail_client.update_trail(Name=trail_name,
                                              IsMultiRegionTrail=True)
    return response
