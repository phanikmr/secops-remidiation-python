import io

import boto3
from PIL import Image


def apply(user_name, access_key=None, secret_key=None, region=None):
    iam_client = boto3.client('iam',
                              region_name=region,
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key)
    try:
        mfa_device = iam_client.create_virtual_mfa_device(
            VirtualMFADeviceName=user_name)
    except iam_client.exceptions.EntityAlreadyExistsException:
        iam = boto3.resource('iam',
                             region_name=region,
                             aws_access_key_id=access_key,
                             aws_secret_access_key=secret_key)
        mfa_device = iam.VirtualMfaDevice('arn:aws:iam::' + boto3.client(
            'sts',
            region_name=region,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key).get_caller_identity()['Account'] +
                                          ':mfa/' + user_name)
        mfa_device.delete()
        mfa_device = iam_client.create_virtual_mfa_device(
            VirtualMFADeviceName=user_name)
    try:
        img = Image.open(io.BytesIO(
            mfa_device['VirtualMFADevice']['QRCodePNG']))
        img.show()
    except Exception as err:  # pylint: disable=broad-except
        print(err)
        print(mfa_device)
    auth_code_1 = input('Please enter Authentication Code 1: ')
    auth_code_2 = input('Please enter Authentication Code 2: ')
    response = iam_client.enable_mfa_device(
        UserName=user_name,
        SerialNumber=mfa_device['VirtualMFADevice']['SerialNumber'],
        AuthenticationCode1=auth_code_1,
        AuthenticationCode2=auth_code_2)
    return response


if __name__ == '__main__':
    print(apply('secops-test'))
