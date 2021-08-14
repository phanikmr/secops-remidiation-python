import aioboto3


async def apply(security_group_id,
                instances_to_update,
                access_key=None,
                secret_key=None,
                region=None):
    async with aioboto3.Session().client('ec2',
                                         aws_access_key_id=access_key,
                                         aws_secret_access_key=secret_key,
                                         region_name=region) as ec2_client:
        async with aioboto3.Session().resource('ec2',
                                               aws_access_key_id=access_key,
                                               aws_secret_access_key=secret_key,
                                               region_name=region) as ec2:
            security_group = await ec2.SecurityGroup(security_group_id)
            new_security_group = await ec2_client.create_security_group(
                Description='clone of ' + security_group_id,
                GroupName='Copy of default security group ' + security_group_id,
                VpcId=await security_group.vpc_id)
            new_security_group_id = new_security_group['GroupId']
            new_security_group = await ec2.SecurityGroup(new_security_group_id)
            await new_security_group.authorize_egress(
                IpPermissions=await security_group.ip_permissions_egress)
            await new_security_group.authorize_ingress(
                IpPermissions=await security_group.ip_permissions)
            instances = await ec2_client.describe_instances(
                InstanceIds=instances_to_update)
            if 'Reservations' in instances:
                for reservation in instances['Reservations']:
                    for instance in reservation['Instances']:
                        security_groups = [new_security_group_id]
                        for group in instance['SecurityGroups']:
                            if group['GroupId'] != security_group_id:
                                security_groups.append(group['GroupId'])
                        await ec2_client.modify_instance_attribute(
                            InstanceId=instance['InstanceId'],
                            Groups=security_groups)

            return new_security_group_id


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    print(
        loop.run_until_complete(
            apply('sg-062b5e12072f4dc31', [
                'i-0f78fa1e21a56c420', 'i-0ff368c159054d537',
                'i-054e5d9a4a47dd69a', 'i-062b19a0650c358b1'
            ])))
