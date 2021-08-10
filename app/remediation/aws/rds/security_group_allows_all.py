import boto3
from remediation.aws.ec2.sg_opens_all_ports_to_all_ingress import \
    apply as modify_ingres


def apply(db_instance_id,
          cidr_ingres_ipv4,
          cidr_ingres_ipv6=None,
          access_key=None,
          secret_key=None,
          region=None):
    rds_client = boto3.client('rds',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              region_name=region)
    response = rds_client.describe_db_instances(
        DBInstanceIdentifier=db_instance_id)
    instance = response['DBInstances'][0]
    security_groups = instance['VpcSecurityGroups']
    for security_group in security_groups:
        modify_ingres(security_group['VpcSecurityGroupId'], cidr_ingres_ipv4,
                      cidr_ingres_ipv6, [0, 65535])

    return response


if __name__ == '__main__':
    print(apply('database-1-instance-1', '10.0.0.0/32'))
