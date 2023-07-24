from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from django.shortcuts import get_object_or_404
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


