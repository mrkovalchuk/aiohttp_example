from aiohttp import web

from apps.users.serializer import UserSerializer
from apps.users.services import UserService


async def create_user(request):
    return web.Response()


class UserView(web.View):
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

    async def post(self) -> web.Response:
        return await create_user(self.request)


async def get_users_list_api(request) -> web.Response:
    pass
