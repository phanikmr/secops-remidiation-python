from .instance_backup_disabled import apply as modify_retention


async def apply(db_instance_id,
                retention_period,
                access_key=None,
                secret_key=None,
                region=None):
    return await modify_retention(db_instance_id, retention_period, access_key,
                                  secret_key, region)
