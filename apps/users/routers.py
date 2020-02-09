from aiohttp import web

from apps.users.api import UserView


uuid_regular = r'\[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}'


def setup_routes(app):
    app.router.add_view('/user_info/{pk}', UserView, name='user-info')
