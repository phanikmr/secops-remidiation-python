import boto3


def apply(security_group_id,
          new_cidr_block_ipv4s,
          new_cidr_block_ipv6s,
          new_ports_range,
          portocol,
          access_key=None,
          secret_key=None,
          region=None):
    ec2_client = boto3.resource('ec2',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)
    security_group = ec2_client.SecurityGroup(security_group_id)

    new_ip_permissions = []
    if new_cidr_block_ipv4s:
        for new_cidr_block_ipv4 in new_cidr_block_ipv4s:
            new_ip_permissions.append({
                'IpProtocol': portocol,
                'FromPort': new_ports_range[0],
                'ToPort': new_ports_range[1],
                'IpRanges': [{
                    'CidrIp': new_cidr_block_ipv4
                }]
            })
    if new_cidr_block_ipv6s:
        for new_cidr_block_ipv6 in new_cidr_block_ipv6s:
            new_ip_permissions.append({
                'IpProtocol': portocol,
                'FromPort': new_ports_range[0],
                'ToPort': new_ports_range[1],
                'Ipv6Ranges': [{
                    'CidrIpv6': new_cidr_block_ipv6
                }]
            })

    response = security_group.authorize_ingress(
        IpPermissions=new_ip_permissions)
    return response


if __name__ == '__main__':
    print(
        apply('sg-06acf2a824596540f', ['0.0.0.0/16'],
              ['2001:db8:3333:4444:5555:6666:7777:8888/128'], [3000, 4000],
              'tcp',
              region='us-east-1'))
