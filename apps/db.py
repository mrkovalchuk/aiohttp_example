import asyncio

import asyncpg
from asyncpg import Connection

from aiohttp_example.settings import config


async def create_tables_with_data(only_data=False):
    conf = config['postgres']
    print('Try to connect')
    conn: Connection = await asyncpg.connect(database=conf['database'],
                                             user=conf['user'],
                                             password=conf['password'],
                                             host=conf['host'],
                                             port=conf['port'])
    if not only_data:
        print('Create table')
        query = '''
                CREATE TABLE users (
                    id SERIAL,
                    full_name varchar(32) NOT NULL
                )
            '''

        await conn.execute(query)

    print('Insert data')
    await insert_data(conn)


async def insert_data(conn):
    await conn.execute('''
        INSERT INTO users VALUES (1, 'User1 User1'), (2, 'User2 User2');
    ''')


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


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(create_tables_with_data(only_data=True))
