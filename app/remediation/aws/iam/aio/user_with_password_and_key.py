from .service_user_with_password import apply as delete_password
from .user_with_multiple_access_keys import apply as delete_key


async def apply(user_name,
                access_key_delete=None,
                access_key=None,
                secret_key=None,
                region=None):
    if access_key_delete:
        return await delete_key(user_name, access_key_delete, access_key,
                                secret_key, region)
    return await delete_password(user_name, access_key, secret_key, region)
