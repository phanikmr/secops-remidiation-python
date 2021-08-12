import aioboto3


async def apply(topic_arn,
                statement_name,
                account_ids,
                actions,
                statement_to_delete_name=None,
                access_key=None,
                secret_key=None,
                region=None):
    async with aioboto3.Session().client('sns',
                                         aws_access_key_id=access_key,
                                         aws_secret_access_key=secret_key,
                                         region_name=region) as sns_client:
        if statement_to_delete_name:
            await sns_client.remove_permission(TopicArn=topic_arn,
                                               Label=statement_to_delete_name)
        response = await sns_client.add_permission(TopicArn=topic_arn,
                                                   Label=statement_name,
                                                   AWSAccountId=account_ids,
                                                   ActionName=actions)
        return response
