from django.forms import ValidationError
from rest_framework import serializers
from rest_framework.status import HTTP_400_BAD_REQUEST
from users.models import User
from rest_framework.serializers import (
    BooleanField,
    CharField,
    ImageField,
    ModelSerializer,
    ValidationError,
)
from .models import Order


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
