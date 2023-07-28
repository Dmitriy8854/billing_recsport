from django.db import models
from services.models import Subscription


class Order(models.Model):
    sum = models.IntegerField()
    subscriptions = models.ForeignKey(Subscription, on_delete=models.PROTECT)
    client = models.ForeignKey("users.User", on_delete=models.PROTECT)
    status = models.CharField(max_length=120)
    order_id = models.CharField(max_length=120)
