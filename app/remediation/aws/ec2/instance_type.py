import time

import boto3


def apply(instance_id,
          new_instance_type,
          start_instance=False,
          access_key=None,
          secret_key=None,
          region=None):
    ec2 = boto3.resource('ec2',
                         aws_access_key_id=access_key,
                         aws_secret_access_key=secret_key,
                         region_name=region)
    instance = ec2.Instance(instance_id)
    while instance.state['Name'] != 'stopped':
        instance.stop()
        time.sleep(3)
        instance = ec2.Instance(instance_id)
    response = instance.modify_attribute(Attribute='instanceType',
                                         Value=new_instance_type)
    if start_instance:
        instance.start()
    return response


if __name__ == '__main__':
    print(apply('i-03b827057c11d7774', 't2.micro', region='us-east-1'))
