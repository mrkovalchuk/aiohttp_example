from typing import Sequence, Dict

from asyncpg.pool import Pool

from apps.users.data import User, UserDataAccess


class UserService:
    def __init__(self, connection_pool: Pool):
        self.db = UserDataAccess(connection_pool)

    async def get_user(self, pk: int) -> User:
        return await self.db.get_user(pk)

    async def get_users_list(self) -> Sequence[User]:
        return await self.db.get_users()

    async def create_user(self, data: Dict) -> User:
        return await self.db.create_user(data)
