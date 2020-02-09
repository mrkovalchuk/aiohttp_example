from asyncpg.pool import Pool

from apps.users.data import User, UserDataAccess


class UserService:
    def __init__(self, connection_pool: Pool):
        self.db = UserDataAccess(connection_pool)

    async def get_user(self, pk: int) -> User:
        return await self.db.get_user(pk)
