import boto3


def apply(db_snapshot_id,
          account_id,
          access_key=None,
          secret_key=None,
          region=None):
    rds_client = boto3.client('rds',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    response = rds_client.modify_db_snapshot_attribute(
        DBSnapshotIdentifier=db_snapshot_id,
        AttributeName='restore',
        ValuesToAdd=[account_id])
    return response
