import boto3

PLAIN_TEXT_PORTS = [80, 119, 20, 21, 23, 143, 110, 25]
ENCRYPTED_PORTS = [443, 563, 989, 990, 992, 993, 995, 465]


def apply(security_group_id, access_key=None, secret_key=None, region=None):
    ec2_client = boto3.resource('ec2',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region)
    security_group = ec2_client.SecurityGroup(security_group_id)
    revoke_list = []
    for ips in security_group.ip_permissions:
        for port in PLAIN_TEXT_PORTS:
            if ips['FromPort'] <= port <= ips['ToPort'] or ips['FromPort'] == -1:
                revoke_list.append(ips)
                break

    response = security_group.revoke_ingress(IpPermissions=revoke_list)
    return response


if __name__ == '__main__':
    print(apply('sg-06acf2a824596540f', region='us-east-1'))
