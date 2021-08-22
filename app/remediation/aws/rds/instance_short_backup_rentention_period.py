from .instance_backup_disabled import apply as modify_retention


def apply(db_instance_id,
          retention_period,
          access_key=None,
          secret_key=None,
          region=None):
    return modify_retention(db_instance_id, retention_period, access_key,
                            secret_key, region)
