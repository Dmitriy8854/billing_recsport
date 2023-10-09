from djoser.serializers import UserSerializer
from rest_framework import serializers
from users.models import User, Group, GroupMember


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ("email", "id", "username", "first_name", "last_name", "role")

class GroupSerializer(serializers.ModelSerializer):
    trainer = serializers.StringRelatedField(many=False, read_only=True)
    class Meta:
        model = Group
        fields = ("groupname", "trainer")


class GroupMemberSerializer(serializers.ModelSerializer):
   # group = serializers.SlugRelatedField(queryset=Group.objects.all(), many=False, slug_field='groupname', read_only=False)
    group = GroupSerializer(many=True, read_only=False)
    sportsman = serializers.StringRelatedField(many=False, read_only=True)
    class Meta:
        model = GroupMember
        fields = ("group", "sportsman")

    # def create(self, validated_data):
    #     groups = self.initial_data.get('group')
    #     sportsman = User.objects.create(**validated_data)

    #     for group in groups:
    #         GroupMember.objects.create(group=group, sportsman=sportsman)
    #     return 

# class GroupMember(models.Model):
#     group = models.ForeignKey(Group, models.PROTECT, "members")
#     sportsman = models.OneToOneField(
#         "users.User", on_delete=models.PROTECT, related_name="group"
#     )
