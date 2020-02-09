from apps.users.api import UserView, get_users_list


def setup_routes(app):
    app.router.add_view('/user_info/{pk}', UserView, name='user-info')
    app.router.add_get('/', get_users_list, name='user-list')
