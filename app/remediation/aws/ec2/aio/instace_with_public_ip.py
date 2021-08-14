import asyncio

import aioboto3


async def apply(instance_id, access_key=None, secret_key=None, region=None):
    async with aioboto3.Session().client('ec2',
                                         aws_access_key_id=access_key,
                                         aws_secret_access_key=secret_key,
                                         region_name=region) as ec2_client:
        ips = await ec2_client.describe_addresses()
        eip_id = None
        for address in ips['Addresses']:
            if 'InstanceId' in address or 'NetworkInterfaceId' in address:
                pass
            else:
                eip_id = address['AllocationId']
                break
        if not eip_id:
            raise Exception(
                'To disassociate public ip require a free temporary elastic IP')
        instance = await ec2_client.describe_instances(
            InstanceIds=[instance_id])
        instance = instance['Reservations'][0]['Instances'][0]
        network_interface_id = instance['NetworkInterfaces'][0][
            'NetworkInterfaceId']
        subnet_id = instance['SubnetId']
        nic_id = await ec2_client.create_network_interface(SubnetId=subnet_id)
        nic_id = nic_id['NetworkInterface']['NetworkInterfaceId']
        await ec2_client.associate_address(
            AllocationId=eip_id, NetworkInterfaceId=network_interface_id)
        await ec2_client.attach_network_interface(
            NetworkInterfaceId=nic_id,
            InstanceId=instance_id,
            DeviceIndex=len(instance['NetworkInterfaces']))
        association_id = await ec2_client.describe_addresses(
            AllocationIds=[eip_id])
        association_id = association_id['Addresses'][0]['AssociationId']
        await ec2_client.disassociate_address(AssociationId=association_id)
        instance = await ec2_client.describe_instances(
            InstanceIds=[instance_id])
        interfaces = instance['Reservations'][0]['Instances'][0][
            'NetworkInterfaces']
        for interface in interfaces:
            if interface['NetworkInterfaceId'] == nic_id:
                attachment_id = interface['Attachment']['AttachmentId']
        await ec2_client.detach_network_interface(AttachmentId=attachment_id)
        status = await ec2_client.describe_network_interfaces(
            NetworkInterfaceIds=[nic_id])
        status = status['NetworkInterfaces'][0]['Status']
        while status != 'available':
            await asyncio.sleep(3)
            status = await ec2_client.describe_network_interfaces(
                NetworkInterfaceIds=[nic_id])
            status = status['NetworkInterfaces'][0]['Status']
        await ec2_client.delete_network_interface(NetworkInterfaceId=nic_id)
        return instance


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(
        loop.run_until_complete(apply('i-05b83214c9726cf6c',
                                      region='us-east-1')))
