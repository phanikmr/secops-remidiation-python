from .instance_type import apply as change_type


async def apply(instance_ids,
                new_instance_types,
                start_instances=False,
                access_key=None,
                secret_key=None,
                region=None):
    for i in range(0, len(instance_ids)):
        await change_type(instance_ids[i], new_instance_types[i],
                          start_instances, access_key, secret_key, region)
