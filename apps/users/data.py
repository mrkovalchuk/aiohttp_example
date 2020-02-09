import string
import uuid
from typing import Sequence, Dict

from asyncpg.pool import Pool


class User:
    __slots__ = {'name', 'surname', 'address', 'id'}

    def __init__(self, name, surname, address, user_id=None):
        self.name: string = name
        self.surname: string = surname
        self.address: string = address
        self.id: uuid = user_id

    def __str__(self):
        return f'{self.id}:{self.name} {self.surname}'

    def to_json(self, fields):
        return {field_name: str(getattr(self, field_name)) for field_name in fields}


class UserDataAccess:
    model = User

    def __init__(self, connection_pool: Pool):
        self.conn_pool = connection_pool

    async def get_user(self, pk):
        async with self.conn_pool.acquire() as connection:
            result = await connection.fetchrow(f'''
                SELECT id as user_id, name, surname, address FROM users
                WHERE users.id = $1
            ''', pk)
            return User(**result)

    async def get_users(self) -> Sequence[User]:
        async with self.conn_pool.acquire() as connection:
            result = await connection.fetch(f'''
                SELECT id as user_id, name, surname, address FROM users
            ''')
            users = [User(**item) for item in result]
            return users

    async def create_user(self, data: Dict) -> User:
        async with self.conn_pool.acquire() as connection:
            result = await connection.fetchrow('''
                INSERT INTO users(name, surname, address) VALUES ($1, $2, $3) RETURNING id
            ''', data['name'], data['surname'], data['address'])

            return User(**data, user_id=result['id'])
