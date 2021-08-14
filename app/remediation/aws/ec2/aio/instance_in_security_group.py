import aioboto3


async def apply(security_group_id,
                instance_ids,
                access_key=None,
                secret_key=None,
                region=None):
    async with aioboto3.Session().client('ec2',
                                         aws_access_key_id=access_key,
                                         aws_secret_access_key=secret_key,
                                         region_name=region) as ec2_client:
        instances = await ec2_client.describe_instances(InstanceIds=instance_ids
                                                       )
        if 'Reservations' in instances:
            for reservation in instances['Reservations']:
                for instance in reservation['Instances']:
                    security_groups = []
                    for group in instance['SecurityGroups']:
                        if group['GroupId'] != security_group_id:
                            security_groups.append(group['GroupId'])
                    await ec2_client.modify_instance_attribute(
                        InstanceId=instance['InstanceId'],
                        Groups=security_groups)

    return instances
