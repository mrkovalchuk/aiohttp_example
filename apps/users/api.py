from aiohttp import web

from apps.users.serializer import UserSerializer, ListUserSerializer
from apps.users.services import UserService
from apps.utils.api import BaseView


class GetUserView(BaseView):
    serializer_class = UserSerializer

    def get_serializer(self):
        return self.serializer_class()

    async def get(self) -> web.Response:
        pool = self.request.app['pool']
        user_service = UserService(pool)
        user = await user_service.get_user(self.request.match_info['pk'])

        serializer = self.get_serializer()
        result = serializer.to_representation(user)

        return web.json_response(result)


class CreateUserView(BaseView):
    serializer_class = ListUserSerializer

    async def post(self) -> web.Response:
        pool = self.request.app['pool']
        user_service = UserService(pool)
        data = await self.request.json()
        user = await user_service.create_user(data)

        serializer = self.get_serializer()
        result = serializer.to_representation(user)

        return web.json_response(result)


async def get_users_list(request) -> web.Response:
    pool = request.app['pool']
    user_service = UserService(pool)
    users = await user_service.get_users_list()

    serializer = ListUserSerializer()
    result = [serializer.to_representation(user) for user in users]

    return web.json_response(result)
