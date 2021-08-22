import time
import uuid

import boto3


def apply(db_instance_identifier,
          new_encrypted_db_instance_identifier,
          kms_key_id,
          access_key=None,
          secret_key=None,
          region=None):
    '''ref:
https://aws.amazon.com/blogs/aws/amazon-rds-update-share-encrypted-snapshots-encrypt-existing-instances/
    '''
    rds_client = boto3.client('rds',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    snapshot_name = db_instance_identifier + '-' + str(uuid.uuid4())
    db_instance_snapshot = rds_client.create_db_snapshot(
        DBSnapshotIdentifier=snapshot_name,
        DBInstanceIdentifier=db_instance_identifier)
    db_instance_snapshot = db_instance_snapshot['DBSnapshot']

    while db_instance_snapshot['Status'] != 'available':
        time.sleep(10)
        db_instance_snapshot = rds_client.describe_db_snapshots(
            DBSnapshotIdentifier=snapshot_name)
        db_instance_snapshot = db_instance_snapshot['DBSnapshots'][0]

    db_instance_snapshot_encrypted = rds_client.copy_db_snapshot(
        SourceDBSnapshotIdentifier=snapshot_name,
        TargetDBSnapshotIdentifier=snapshot_name + '-encrypted',
        KmsKeyId=kms_key_id)
    db_instance_snapshot_encrypted = db_instance_snapshot_encrypted[
        'DBSnapshot']
    while db_instance_snapshot_encrypted['Status'] != 'available':
        time.sleep(10)
        db_instance_snapshot_encrypted = rds_client.describe_db_snapshots(
            DBSnapshotIdentifier=snapshot_name + '-encrypted')
        db_instance_snapshot_encrypted = db_instance_snapshot_encrypted[
            'DBSnapshots'][0]
    response = rds_client.restore_db_instance_from_db_snapshot(
        DBInstanceIdentifier=new_encrypted_db_instance_identifier,
        DBSnapshotIdentifier=snapshot_name + '-encrypted')
    return response


if __name__ == '__main__':
    print(
        apply('database-2', 'database-2-encrypted',
              '13515679-8aba-41b0-9158-2af26ad8a085'))
