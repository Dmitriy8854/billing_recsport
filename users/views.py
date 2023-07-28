from django.shortcuts import render

# Create your views here.
from djoser.views import UserViewSet

from .serializers import CustomUserSerializer


class CustomUserViewSet(UserViewSet):
    pass
