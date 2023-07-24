from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from django.shortcuts import get_object_or_404
from .models import Subscription
from .serializers import SubscriptionSerializer
import base64
import json
import requests


class SubscriptionViewSet(GenericViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    # Create your views here.

    def create(self, request):
        user = "admin"  # Логин в личном кабинете PayKeeper
        password = "json"  # Соответствующий логину пароль
        base64_auth = base64.b64encode(
            f"{user}:{password}".encode()
        ).decode()  # Формируем base64 хэш

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic " + base64_auth,
        }

        response = requests.post(url)
        data = json.loads(response.text)
        return Response({url: data[url]})


user = "json"  # Логин в личном кабинете PayKeeper
password = "json"  # Соответствующий логину пароль
base64_auth = base64.b64encode(
    f"{user}:{password}".encode()
).decode()  # Формируем base64 хэш

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": "Basic " + base64_auth,
}

server_paykeeper = "demo.paykeeper.ru"  # Укажите адрес вашего сервера PayKeeper

# Готовим первый запрос на получение токена
uri = "/info/settings/token/"  # Запрос на получение токена
url = f"http://{server_paykeeper}{uri}"

response = requests.get(url, headers=headers)
p_array = response.json()
if "token" in p_array:
    token = p_array["token"]
else:
    exit("Failed to retrieve token")

# Готовим к выполнению запроса на добавление email в список рассылки
email = "example@paykeeper.ru"  # Почта для добавления
uri = "/change/organization/addreportemail/"  # Запрос 5.3 JSON API
url = f"http://{server_paykeeper}{uri}"

payload = {
    "token": token,
    "email": email,
}

response = requests.post(url, headers=headers, data=payload)
result = response.json()


class SubscriptionViewSet(GenericViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    @action(methods=["post"], detail=False, url_path=response)
    def send_request(self, request):
        subscription = Subscription.objects.all()
        serializer = self.get_serializer(subscription)
        return Response(serializer.data)
