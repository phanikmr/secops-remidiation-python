import aioboto3

PLAIN_TEXT_PORTS = [80, 119, 20, 21, 23, 143, 110, 25]
ENCRYPTED_PORTS = [443, 563, 989, 990, 992, 993, 995, 465]


async def apply(security_group_id,
                access_key=None,
                secret_key=None,
                region=None):
    session = aioboto3.Session()
    async with session.resource('ec2',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region) as ec2_client:
        security_group = await ec2_client.SecurityGroup(security_group_id)
        revoke_list = []
        for ips in await security_group.ip_permissions:
            for port in PLAIN_TEXT_PORTS:
                if ips['FromPort'] <= port <= ips['ToPort'] or ips[
                        'FromPort'] == -1:
                    revoke_list.append(ips)
                    break

        response = await security_group.revoke_ingress(IpPermissions=revoke_list
                                                      )
        return response


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    print(
        loop.run_until_complete(
            apply('sg-06acf2a824596540f', region='us-east-1')))
