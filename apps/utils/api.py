from aiohttp import web


class Serializer:
    def to_representation(self, instance):
        raise NotImplementedError


class BaseView(web.View):
    serializer_class = Serializer

    def get_serializer(self):
        return self.serializer_class()
