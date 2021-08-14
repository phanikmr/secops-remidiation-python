import boto3


def apply(security_group_id,
          new_cidr_block_ipv4,
          new_cidr_block_ipv6,
          new_ports_range,
          access_key=None,
          secret_key=None,
          region=None):
    '''restricts inbound rules to specific IP & ports'''
    ec2_client = boto3.resource('ec2',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)
    security_group = ec2_client.SecurityGroup(security_group_id)
    revoke_list = []
    new_ip_permissions = []
    for ips in security_group.ip_permissions_egress:
        if ips['IpRanges'] and ips['IpRanges'][0]['CidrIp'] == '0.0.0.0/0':
            revoke_list.append(ips)
            new_ip_permissions.append({
                'IpProtocol': ips['IpProtocol'],
                'FromPort': new_ports_range[0],
                'ToPort': new_ports_range[1],
                'IpRanges': [{
                    'CidrIp': new_cidr_block_ipv4
                }]
            })
            continue
        if ips['Ipv6Ranges'] and ips['Ipv6Ranges'][0]['CidrIpv6'] == '::/0':
            revoke_list.append(ips)
            new_ip_permissions.append({
                'IpProtocol': ips['IpProtocol'],
                'FromPort': new_ports_range[0],
                'ToPort': new_ports_range[1],
                'Ipv6Ranges': [{
                    'CidrIpv6': new_cidr_block_ipv6
                }]
            })

    response = security_group.revoke_egress(IpPermissions=revoke_list)
    print(response)
    response = security_group.authorize_egress(IpPermissions=new_ip_permissions)
    return response


if __name__ == '__main__':
    print(
        apply('sg-06acf2a824596540f',
              '0.0.0.0/16',
              '2001:db8:3333:4444:5555:6666:7777:8888/128', [3000, 4000],
              region='us-east-1'))
