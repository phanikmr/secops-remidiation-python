import aioboto3


async def apply(db_instance_identifier,
                ca_certificate_authority='rds-ca-2019',
                access_key=None,
                secret_key=None,
                region=None):
    '''ref:
    https://aws.amazon.com/blogs/database/amazon-rds-customers-update-your-ssl-tls-certificates-by-february-5-2020/

    '''
    async with aioboto3.Session().client('rds',
                                         aws_access_key_id=access_key,
                                         aws_secret_access_key=secret_key,
                                         region_name=region) as rds_client:
        response = await rds_client.modify_db_instance(
            DBInstanceIdentifier=db_instance_identifier,
            CACertificateIdentifier=ca_certificate_authority)
        return response
