import aioboto3


async def apply(access_key=None, secret_key=None, region=None):
    session = aioboto3.Session()
    async with session.client('iam',
                              region_name=region,
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key) as iam_client:

        password_policy = await iam_client.get_account_password_policy()
        password_policy = password_policy['PasswordPolicy']
        response = await iam_client.update_account_password_policy(
            MinimumPasswordLength=password_policy['MinimumPasswordLength'],
            RequireSymbols=password_policy['RequireSymbols'],
            RequireNumbers=password_policy['RequireNumbers'],
            RequireUppercaseCharacters=password_policy[
                'RequireUppercaseCharacters'],
            RequireLowercaseCharacters=password_policy[
                'RequireLowercaseCharacters'],
            AllowUsersToChangePassword=password_policy[
                'AllowUsersToChangePassword'],
            MaxPasswordAge=password_policy['MaxPasswordAge'],
            PasswordReusePrevention=password_policy['PasswordReusePrevention'],
            HardExpiry=True)
    return response
