import boto3


def apply(security_group_id,
          instances_to_update,
          access_key=None,
          secret_key=None,
          region=None):
    ec2_client = boto3.client('ec2',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    ec2 = boto3.resource('ec2',
                         aws_access_key_id=access_key,
                         aws_secret_access_key=secret_key,
                         region_name=region)
    security_group = ec2.SecurityGroup(security_group_id)
    new_security_group = ec2_client.create_security_group(
        Description='clone of ' + security_group_id,
        GroupName='Copy of default security group ' + security_group_id,
        VpcId=security_group.vpc_id)
    new_security_group_id = new_security_group['GroupId']
    new_security_group = ec2.SecurityGroup(new_security_group_id)
    new_security_group.authorize_egress(
        IpPermissions=security_group.ip_permissions_egress)
    new_security_group.authorize_ingress(
        IpPermissions=security_group.ip_permissions)
    instances = ec2_client.describe_instances(InstanceIds=instances_to_update)
    if 'Reservations' in instances:
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                security_groups = [new_security_group_id]
                for group in instance['SecurityGroups']:
                    if group['GroupId'] != security_group_id:
                        security_groups.append(group['GroupId'])
                ec2_client.modify_instance_attribute(
                    InstanceId=instance['InstanceId'], Groups=security_groups)

    return new_security_group_id


if __name__ == '__main__':
    print(
        apply('sg-0d6f6c79', [
            'i-0f78fa1e21a56c420', 'i-0ff368c159054d537', 'i-054e5d9a4a47dd69a',
            'i-062b19a0650c358b1'
        ]))
