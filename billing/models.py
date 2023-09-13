from django.db import models
from services.models import Subscription
from uuid import uuid4
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


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


class TEMPORARY(models.TextChoices):
    BASE_MINUTE = "BASE_MINUTE", "Базовая минута"
    BASE_HOUR = "BASE_HOUR", "Базовый час"


class MONTHLY(models.TextChoices):
    BASE1 = "BASE1", "Временная"
    BASE2 = "BASE2", "Месячная"
    BASE3 = "BASE3", "Месячная"


class SubscriptionDetail(models.TextChoices):
    TEMPORARY = "TEMPORARY", "Временная"
    MONTHLY = models.CharField(
        choices=SubscriptionDetail.choices,
        max_length=120,
        default=SubscriptionDetail.MONTHLY.value,
    )


class Product(models.TextChoices):
    SENSORS = "SENSORS", "Датчики"
    SUBSCRIPTION = models.CharField(
        choices=SubscriptionDetail.choices,
        max_length=120,
        default=SubscriptionDetail.MONTHLY.value,
    )


class MPTTMeta:
    order_insertion_by = ["name"]


class Tarif(MPTTModel):
    LEVEL1 = "LEVEL1"
    LEVEL2 = "LEVEL2"
    LEVEL3 = "LEVEL3"

    type_choices = [
        (LEVEL1, _("LEVEL1")),
        (LEVEL2, _("LEVEL2")),
        (LEVEL3, _("LEVEL3")),
    ]

    name = models.CharField(max_length=100, unique=True)
    types = models.IntegerField(choices=type_choices, max_length=50)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )


class MPTTMeta:
    order_insertion_by = ["name"]


class TarifDetail(TestCase):
    name = models.CharField(max_length=100, unique=True)
    types = models.IntegerField(choices=type_choices, max_length=50)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )


class MPTTMeta:
    order_insertion_by = ["name"]
