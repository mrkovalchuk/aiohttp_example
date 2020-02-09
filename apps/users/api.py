from aiohttp import web


async def get_user_api(request) -> web.Response:
    return web.Response()


async def create_user(request):
    return web.Response()


class UserView(web.View):
    async def get(self) -> web.Response:
        return await get_user_api(self.request)

    async def post(self) -> web.Response:
        return await create_user(self.request)


async def get_users_list_api(request) -> web.Response:
    pass
