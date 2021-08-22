import aioboto3


async def apply(domain, access_key=None, secret_key=None, region=None):
    async with aioboto3.Session().client('ses',
                                         aws_access_key_id=access_key,
                                         aws_secret_access_key=secret_key,
                                         region_name=region) as ses_client:
        response = await ses_client.verify_domain_dkim(Domain=domain)
        return response
