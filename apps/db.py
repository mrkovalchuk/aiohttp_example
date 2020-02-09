import asyncio

import asyncpg


async def init_pg(app):
    conf = app['config']['postgres']
    connection_pool = await asyncpg.create_pool(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
    )

    app['pool'] = connection_pool


async def close_pg(app):
    await app['pool'].coroutineclose()
