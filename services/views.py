from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from django.shortcuts import get_object_or_404
from .models import Subscription
from billing.models import Order
from .serializers import SubscriptionSerializer
import base64
import json
import requests
from .tasks import pay_status
from .utils import create_pay
from billing.serializers import OrderSerializer
from rest_framework.response import Response


class OrderViewSet(GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(client=request.user)
        order = serializer.instance
        pay_id, pay_url = create_pay(
            clientid=order.client_id,
            orderid=order.order_id,
            client_email=order.client.email,
            service_name=order.subscription.name,
            client_phone=order.client.phone,
        )
        order.invoice_id = pay_id
        order.payment_url = pay_url
        order.save()
        return Response(serializer.data)


