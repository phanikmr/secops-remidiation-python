import aioboto3


async def apply(user_name,
                certificate_thumbprint,
                access_key=None,
                secret_key=None,
                region=None):
    session = aioboto3.Session()
    async with session.client('iam',
                              region_name=region,
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key) as iam_client:
        response = await iam_client.update_signing_certificate(
            CertificateId=certificate_thumbprint,
            Status='Inactive',
            UserName=user_name)
    return response
