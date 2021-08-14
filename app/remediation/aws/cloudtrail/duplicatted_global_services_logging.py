import boto3


def apply(duplicate_trail_name,
          stop_logging=False,
          access_key=None,
          secret_key=None,
          region=None):
    cloudtrail_client = boto3.client('cloudtrail',
                                     aws_access_key_id=access_key,
                                     aws_secret_access_key=secret_key,
                                     region_name=region)
    response = cloudtrail_client.update_trail(Name=duplicate_trail_name,
                                              IsMultiRegionTrail=False)
    if stop_logging:
        cloudtrail_client.stop_logging(Name=duplicate_trail_name)
    return response
