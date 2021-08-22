import boto3


def apply(network_acl_id,
          rule_number,
          cidr_block,
          port_range,
          protocol,
          access_key=None,
          secret_key=None,
          region=None):
    vpc_client = boto3.client('ec2',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    response = vpc_client.replace_network_acl_entry(CidrBlock=cidr_block,
                                                    Egress=False,
                                                    NetworkAclId=network_acl_id,
                                                    PortRange={
                                                        'From': port_range[0],
                                                        'To': port_range[1]
                                                    },
                                                    Protocol=protocol,
                                                    RuleAction='allow',
                                                    RuleNumber=rule_number)
    return response
