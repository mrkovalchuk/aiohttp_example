import asyncio

import asyncpg
from asyncpg import Connection

from aiohttp_example.settings import config


create_user_table_query = '''
    CREATE TABLE users (
        id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
        name varchar(32) NOT NULL,
        surname varchar(32) NOT NULL,
        address varchar(64) NOT NULL
    )
'''


async def initialize_tables(only_data=False, drop_db=True):
    conf = config['postgres']
    conn: Connection = await asyncpg.connect(database=conf['database'],
                                             user=conf['user'],
                                             password=conf['password'],
                                             host=conf['host'],
                                             port=conf['port'])

    if drop_db:
        await conn.execute('''
            DROP SCHEMA public CASCADE;
            CREATE SCHEMA public;
        ''')

        # Extension for uuid
        await conn.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

    tables = [create_user_table_query]

    if not only_data:
        for table_query in tables:
            await conn.execute(table_query)

    await _insert_data(conn)
    await conn.close()


async def _insert_data(conn):
    await conn.execute('''
        INSERT INTO users VALUES (uuid_generate_v4(), 'User1', 'Userovich', 'Moscow, 1905, 15/1'),
                                 (uuid_generate_v4(), 'User2', 'Userovich2', 'Volgograd, Pushkinskaya, 28/3');
    ''')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(initialize_tables(drop_db=True))
