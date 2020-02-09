from apps.users.api import get_user_api


uuid_regular = r'\[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}'


def setup_routes(app):
    app.router.add_get(rf'/user_info/{{pk:{uuid_regular}}}', get_user_api, name='user-info')
