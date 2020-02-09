from typing import Sequence

from apps.users.data import User


class UserSerializer:
    model = User
    fields = User.__slots__
    exclude_fields = {'id'}

    def _represented_fields(self):
        return self.fields - self.exclude_fields

    def to_internal_value(self, data: Sequence[dict]):
        return [User(**item) for item in data]

    def to_representation(self, instance: User):
        return instance.to_json(self._represented_fields())


class ListUserSerializer(UserSerializer):
    exclude_fields = set()
