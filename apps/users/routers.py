from apps.users.api import get_users_list_api


def setup_routes(app):
    app.router.add_get('/', get_users_list_api)
