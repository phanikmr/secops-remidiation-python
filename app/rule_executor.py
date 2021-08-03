import asyncio

from app.remediation.aws.cloudtrail import (no_global_services_logging,
                                            no_log_file_validation, no_logging,
                                            not_configured)
from app.remediation.aws.cloudtrail.aio import \
    no_global_services_logging as aio_no_global_services_logging
from app.remediation.aws.cloudtrail.aio import \
    no_log_file_validation as aio_no_log_file_validation
from app.remediation.aws.cloudtrail.aio import no_logging as aio_no_logging
from app.remediation.aws.cloudtrail.aio import \
    not_configured as aio_not_configured


def cloudtrail_rules():

    print(no_global_services_logging.apply('test-trail', region='ap-south-1'))
    print(no_log_file_validation.apply('test-trail', region='ap-south-1'))

    print(
        not_configured.apply('phani-trail',
                             'phani-cloudtrail-bucket',
                             create_bucket=False,
                             region='ap-south-1'))
    print(no_logging.apply('test-trail', region='ap-south-1'))


def async_cloudtrail_rules():
    loop = asyncio.get_event_loop()

    print(
        loop.run_until_complete(
            aio_no_global_services_logging.apply('test-trail',
                                                 region='ap-south-1')))
    print(
        loop.run_until_complete(
            aio_no_log_file_validation.apply('test-trail',
                                             region='ap-south-1')))

    print(
        loop.run_until_complete(
            aio_not_configured.apply('phani-trail',
                                     'phani-cloudtrail-bucket',
                                     region='ap-south-1')))
    print(
        loop.run_until_complete(
            aio_no_logging.apply('test-trail', region='ap-south-1')))
