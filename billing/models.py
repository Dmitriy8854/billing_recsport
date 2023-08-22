from django.db import models
from services.models import Subscription
from uuid import uuid4


class OrderStatus(models.TextChoices):
    CREATE = "CREATE", "Создан"
    SUCCESS = "SUCCESS", "Успешно завершен"
    CANCEL = "CANCEL", "Отменен"


class Order(models.Model):
    sum = models.IntegerField()
    subscription = models.ForeignKey(Subscription, on_delete=models.PROTECT)
    client = models.ForeignKey("users.User", on_delete=models.PROTECT)
    status = models.CharField(
        choices=OrderStatus.choices, max_length=120, default=OrderStatus.CREATE.value
    )
    order_id = models.CharField(max_length=120, default=uuid4)
    invoice_id = models.CharField(max_length=120, default="")
    payment_url = models.CharField(max_length=120, default="")

    def __str__(self):
        return f"Заказ: {self.client - self.subscription}"


class Debit(models.Model):
    sum = models.IntegerField()
    client = models.ForeignKey("users.User", on_delete=models.PROTECT)
    description = models.TextField()
