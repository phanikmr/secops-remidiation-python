from .sg_whitelist_aws_ip_from_banned_region import apply as add_ingress_ips


async def apply(security_group_id,
                new_cidr_block_ipv4s,
                new_cidr_block_ipv6s,
                new_ports_range,
                portocol,
                access_key=None,
                secret_key=None,
                region=None):
    return await add_ingress_ips(security_group_id, new_cidr_block_ipv4s,
                                 new_cidr_block_ipv6s, new_ports_range,
                                 portocol, access_key, secret_key, region)
