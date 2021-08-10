import boto3


def apply(cluster_id, access_key=None, secret_key=None, region=None):
    redshift_client = boto3.client('redshift',
                                   aws_access_key_id=access_key,
                                   aws_secret_access_key=secret_key,
                                   region_name=region)
    response = redshift_client.modify_db_instance(ClusterIdentifier=cluster_id,
                                                  PubliclyAccessible=False)
    return response
