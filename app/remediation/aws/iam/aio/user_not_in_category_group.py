import aioboto3


async def apply(user_name,
                user_group,
                access_key=None,
                secret_key=None,
                region=None):
    session = aioboto3.Session()
    async with session.client('iam',
                              region_name=region,
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key) as iam_client:
        response = await iam_client.add_user_to_group(UserName=user_name,
                                                      GroupName=user_group)
        return response


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(apply('secops-test', 's3access')))
