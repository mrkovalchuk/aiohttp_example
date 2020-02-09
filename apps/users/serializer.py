from apps.users.data import User
from apps.utils.api import Serializer


class UserSerializer(Serializer):
    model = User
    fields = User.__slots__
    exclude_fields = {'id'}

    def _represented_fields(self):
        return self.fields - self.exclude_fields

    def to_representation(self, instance: User):
        return instance.to_json(self._represented_fields())


class ListUserSerializer(UserSerializer):
    exclude_fields = set()
