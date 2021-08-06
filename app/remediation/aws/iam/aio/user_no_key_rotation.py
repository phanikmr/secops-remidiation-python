import pprint

import aioboto3


async def apply(user_name, access_key=None, secret_key=None, region=None):
    session = aioboto3.Session()
    async with session.client('iam',
                              region_name=region,
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key) as iam_client:
        keys = await iam_client.list_access_keys(UserName=user_name)
        new_key = await iam_client.create_access_key(UserName=user_name)
        pprint.pprint(new_key)
        print('Save the keys. Will ne shown only once')
        for key in keys['AccessKeyMetadata']:
            await iam_client.delete_access_key(UserName=user_name,
                                               AccessKeyId=key['AccessKeyId'])
        return new_key


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(apply('secops-test')))
