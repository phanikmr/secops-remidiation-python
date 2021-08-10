import boto3


def apply(db_instance_id, access_key=None, secret_key=None, region=None):
    rds_client = boto3.client('rds',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    response = rds_client.modify_db_instance(
        DBInstanceIdentifier=db_instance_id, MultiAZ=True)
    return response


if __name__ == '__main__':
    print(apply('database-1-instance-1'))
