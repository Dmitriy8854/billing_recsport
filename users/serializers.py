from djoser.serializers import UserSerializer
from .models import Group


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ("email", "id", "username", "first_name", "last_name", "role")


class GroupSerializer(UserSerializer):
    class Meta:
        model = Group
        fields = ("groupname", "admin", "sportsmen", "date_creation")
