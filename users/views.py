from django.shortcuts import render

# Create your views here.
from djoser.views import UserViewSet
from .models import User
from .serializers import CustomUserSerializer, GroupSerializer


class CustomUserViewSet(UserViewSet):
    pass


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer

    def get_queryset(self):
        # Получаем id тренера/админа из эндпоинта
        user_id = self.kwargs.get("user_id")
        # И отбираем группу, где он админ
        new_queryset = Group.objects.filter(admin=user_id)
        return new_queryset

        sportsmen = User.objects.filter(role=ROLE_CHOICES.SPORTSMEN.value)

    @action(detail=False)
    def filling_group(self):
        admin = request.user
        sportsmen = User.objects.filter(role=ROLE_CHOICES.SPORTSMEN.value)

        serializer = GroupSerializer(sportsmen, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        Group.objects.create(admin=admin, sportsmen=sportsmen)
        return Response(serializer.data, status=HTTP_201_CREATED)
