from django.db import models


class Order(models.Model):
    sum = models.IntegerField()
    subscriptions = models.ForeignKey(
        "services.Subscriptions", on_delete=models.PROTECT
    )
    client = models.ForeignKey("users.User", on_delete=models.PROTECT)
    status = models.CharField(max_length=120)
    order_id = models.CharField(max_length=120)
