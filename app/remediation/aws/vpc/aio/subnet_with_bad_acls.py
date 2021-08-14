import json

import aioboto3


async def apply(endpoint_id,
                policy_doc,
                access_key=None,
                secret_key=None,
                region=None):
    async with aioboto3.Session().client('ec2',
                                         aws_access_key_id=access_key,
                                         aws_secret_access_key=secret_key,
                                         region_name=region) as vpc_client:
        response = await vpc_client.modify_vpc_endpoint(
            VpcEndpointId=endpoint_id, PolicyDocument=json.dumps(policy_doc))
        return response


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    print(
        loop.run_until_complete(
            apply(
                'vpce-32ba3c5b', {
                    'Statement': [{
                        'Action': '*',
                        'Effect': 'Allow',
                        'Resource': '*',
                        'Principal': '*'
                    }]
                })))
