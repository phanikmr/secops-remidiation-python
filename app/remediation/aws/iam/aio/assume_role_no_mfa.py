from .assume_role_lacks_external_id_and_mfa import \
    apply as role_update_policy_for_mfa


async def apply(role_name, access_key=None, secret_key=None, region=None):
    return await role_update_policy_for_mfa(role_name, None, access_key,
                                            secret_key, region)
