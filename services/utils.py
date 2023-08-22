import base64
import requests
import json
import os
from dotenv import load_dotenv

# test_work_with_secrets.py

load_dotenv()

user = os.getenv("PAYMENT_USER")
password = os.getenv("PAYMENT_PASSWORD")


def create_pay(clientid, orderid, client_email, service_name, client_phone):
    # user = os.getenv("USER")  # Логин в личном кабинете PayKeeper
    # password = os.getenv("PASSWORD")  # Соответствующий логину пароль

    base64_auth = base64.b64encode(
        f"{user}:{password}".encode()
    ).decode()  # Формируем base64 хэш

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + base64_auth,
    }
    server_paykeeper = "https://intelp-vk.server.paykeeper.ru"
    payload = {
        "pay_amount": 42.50,
        "clientid": clientid,
        "orderid": orderid,
        "client_email": client_email,
        "service_name": service_name,
        "client_phone": client_phone,
    }

    uri = "/info/settings/token/"
    response = requests.get(server_paykeeper + uri, headers=headers)
    data = json.loads(response.text)
    token = data["token"]

    uri = "/change/invoice/preview/"
    response = requests.post(
        server_paykeeper + uri, headers=headers, data={**payload, "token": token}
    )
    data = json.loads(response.text)
    return (data["invoice_id"], data["invoice_url"])


def get_pay_status(invoice_id):
    # user = "******"  - Логин в личном кабинете PayKeeper
    # password = "*********"  - Соответствующий логину пароль
    base64_auth = base64.b64encode(
        f"{user}:{password}".encode()
    ).decode()  # Формируем base64 хэш

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + base64_auth,
    }
    server_paykeeper = "https://intelp-vk.server.paykeeper.ru"

    # uri = "/info/invoice/byid/invoice_id/"

    uri = "/info/invoice/byid/?id=" + invoice_id
    response = requests.get(server_paykeeper + uri, headers=headers)
    print(response.status_code)
    print(response.text)
    # data = json.loads(response.text)
    data = json.loads(response.text)
    print(data)
    return data["status"]


clientid = "Иванов Иван Иванович"
orderid = "Заказ № 10"
client_email = "234@mail.ru"
service_name = "Услуга"
client_phone = "89254474441"


if __name__ == "__main__":
    invoice_id, invoice_url = create_pay(
        clientid, orderid, client_email, service_name, client_phone
    )
    print(get_pay_status(invoice_id))
