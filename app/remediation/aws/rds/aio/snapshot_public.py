import aioboto3


async def apply(db_snapshot_id,
                account_id,
                access_key=None,
                secret_key=None,
                region=None):
    session = aioboto3.Session()
    async with session.client('rds',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region) as rds_client:
        response = await rds_client.modify_db_snapshot_attribute(
            DBSnapshotIdentifier=db_snapshot_id,
            AttributeName='restore',
            ValuesToAdd=[account_id])
        return response
