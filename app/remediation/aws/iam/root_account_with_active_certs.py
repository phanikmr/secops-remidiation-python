import boto3


def apply(user_name,
          certificate_thumbprint,
          access_key=None,
          secret_key=None,
          region=None):
    iam_client = boto3.client('iam',
                              region_name=region,
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key)
    response = iam_client.update_signing_certificate(
        CertificateId=certificate_thumbprint,
        Status='Inactive',
        UserName=user_name)
    return response


if __name__ == '__main__':
    print(apply('secops-test', '2DMPEOBSVKAQA3JAX6NCBROOBPTKPPW4'))
