import aioboto3


async def apply(account_id=None, access_key=None, secret_key=None, region=None):
    async with aioboto3.Session().client('s3control',
                                         aws_access_key_id=access_key,
                                         aws_secret_access_key=secret_key,
                                         region_name=region) as s3_client:
        if not account_id:
            async with aioboto3.Session().client(
                    'sts',
                    aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key,
                    region_name=region) as sts_client:
                account_id = await sts_client.get_caller_identity()
                account_id = account_id['Account']
        response = await s3_client.put_public_access_block(
            AccountId=account_id,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            })
    return response


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(apply()))
