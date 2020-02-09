from apps.users.api import GetUserView, get_users_list, CreateUserView


def setup_routes(app):
    app.router.add_view('/user_info/', CreateUserView, name='create-user')
    app.router.add_view('/user_info/{pk}', GetUserView, name='user-info')
    app.router.add_get('/', get_users_list, name='user-list')
