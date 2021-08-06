import boto3


def apply(access_key=None, secret_key=None, region=None):
    iam_client = boto3.client('iam',
                              region_name=region,
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key)

    password_policy = iam_client.get_account_password_policy()
    password_policy = password_policy['PasswordPolicy']
    response = iam_client.update_account_password_policy(
        MinimumPasswordLength=password_policy['MinimumPasswordLength'],
        RequireSymbols=password_policy['RequireSymbols'],
        RequireNumbers=password_policy['RequireNumbers'],
        RequireUppercaseCharacters=password_policy[
            'RequireUppercaseCharacters'],
        RequireLowercaseCharacters=True,
        AllowUsersToChangePassword=password_policy[
            'AllowUsersToChangePassword'],
        MaxPasswordAge=password_policy['MaxPasswordAge'],
        PasswordReusePrevention=password_policy['PasswordReusePrevention'],
        HardExpiry=password_policy['HardExpiry'])
    return response
