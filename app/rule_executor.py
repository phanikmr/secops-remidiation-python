import asyncio


def cloudtrail_rules():
    from app.remediation.aws.cloudtrail import no_global_services_logging  # pylint: disable=C
    from app.remediation.aws.cloudtrail import no_log_file_validation  # pylint: disable=C
    from app.remediation.aws.cloudtrail import not_configured  # pylint: disable=C
    from app.remediation.aws.cloudtrail import no_logging  # pylint: disable=C

    print(no_global_services_logging.apply('test-trail', region='ap-south-1'))
    print(no_log_file_validation.apply('test-trail', region='ap-south-1'))

    print(
        not_configured.apply('phani-trail',
                             'phani-cloudtrail-bucket',
                             create_bucket=False,
                             region='ap-south-1'))
    print(no_logging.apply('test-trail', region='ap-south-1'))


def async_cloudtrail_rules():
    from app.remediation.aws.cloudtrail.aio import no_global_services_logging  # pylint: disable=C
    from app.remediation.aws.cloudtrail.aio import no_log_file_validation  # pylint: disable=C
    from app.remediation.aws.cloudtrail.aio import not_configured  # pylint: disable=C
    from app.remediation.aws.cloudtrail.aio import no_logging  # pylint: disable=C
    loop = asyncio.get_event_loop()

    print(
        loop.run_until_complete(
            no_global_services_logging.apply('test-trail',
                                             region='ap-south-1')))
    print(
        loop.run_until_complete(
            no_log_file_validation.apply('test-trail', region='ap-south-1')))

    print(
        loop.run_until_complete(
            not_configured.apply('phani-trail',
                                 'phani-cloudtrail-bucket',
                                 region='ap-south-1')))
    print(
        loop.run_until_complete(
            no_logging.apply('test-trail', region='ap-south-1')))
