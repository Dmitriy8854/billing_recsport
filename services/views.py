from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
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
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy

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


# Главная страница
def index(request):
    return HttpResponse("Главная страница")


class SelectProduct(TemplateView):
    template_name = ''


class AddSubscription(TemplateView):
    template_name = ''
    def post(self, request, *args, **kwargs):
        if 'cart' in request.session:
            cart = request.session['cart']
        else:
            cart = []
        subscription = {}
        type = request.POST.get('type', None)
        count = request.POST.get('count', None)
        subscription['count'] = count
        subscription['type'] = type
        cart.append(subscription)
        request.session['cart'] = cart
        return redirect(reverse_lazy('cart'))

class AddTracker(TemplateView):
    template_name = ''

class Cart(TemplateView):
    template_name = ''
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data['cart'] = self.request.session['cart']
        return data

class Sale(TemplateView):
    template_name = ''
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data['cart'] = self.request.session['cart']
        return data
    def post(self, request, *args, **kwargs):
        order = Order.objects.create(
            sum =
            client = self.request.user
            subscription =
            ubscription
            status = models.CharField(
        choices=OrderStatus.choices, max_length=120, default=OrderStatus.CREATE.value
    )
    order_id = models.CharField(max_length=120, default=uuid4)
    invoice_id = models.CharField(max_length=120, default="")
    payment_url = models.CharField(max_length=120, default="")
    amount_tracker = models.IntegerField(default=0)
        )
        
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