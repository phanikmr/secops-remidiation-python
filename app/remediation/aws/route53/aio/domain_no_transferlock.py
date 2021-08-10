import aioboto3


async def apply(doamin, access_key=None, secret_key=None, region=None):
    session = aioboto3.Session()
    async with session.client('route53domains',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region) as route53_client:
        response = await route53_client.enable_domain_transfer_lock(
            DomainName=doamin)
        return response
