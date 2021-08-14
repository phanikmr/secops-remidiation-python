import asyncio

import aioboto3


async def apply(instance_id,
                new_instance_type,
                start_instance=False,
                access_key=None,
                secret_key=None,
                region=None):
    async with aioboto3.Session().resource('ec2',
                                           aws_access_key_id=access_key,
                                           aws_secret_access_key=secret_key,
                                           region_name=region) as ec2:
        instance = await ec2.Instance(instance_id)
        state = await instance.state
        while state['Name'] != 'stopped':
            await instance.stop()
            await asyncio.sleep(3)
            instance = await ec2.Instance(instance_id)
            state = await instance.state
        response = await instance.modify_attribute(Attribute='instanceType',
                                                   Value=new_instance_type)
        if start_instance:
            await instance.start()
        return response


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    print(
        loop.run_until_complete(
            apply('i-03b827057c11d7774', 't2.nano', region='us-east-1')))
