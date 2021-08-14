from .sg_opens_all_ports_to_all_egress import apply as egress
from .sg_opens_all_ports_to_all_ingress import apply as ingress


async def apply(security_group_id,
                ipv4_inbound,
                ipv4_outbound,
                ports: list,
                access_key=None,
                secret_key=None,
                region=None):

    res_1 = await egress(security_group_id, ipv4_outbound, None, ports,
                         access_key, secret_key, region)
    res_2 = await ingress(security_group_id, ipv4_inbound, None, ports,
                          access_key, secret_key, region)
    return [res_1, res_2]
