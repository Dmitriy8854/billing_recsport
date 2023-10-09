from django.db import models


class SubscriptionChoices(models.TextChoices):
    MOUNTH = "MOUNTH", "месячная"
    TIME = "TIME", "поминутная"


class Tarif(models.Model):
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=120, choices=SubscriptionChoices.choices)
    price = models.IntegerField(default=0)


# Create your models here.
class Subscription(models.Model):
    sportsman = models.OneToOneField(
        "users.User", on_delete=models.PROTECT, related_name="subscriptions"
    )
    type = models.CharField(max_length=120, choices=SubscriptionChoices.choices, default=SubscriptionChoices.MOUNTH.value)
    count_minute = models.IntegerField(default=0)
    start = models.DateTimeField(default=None, null=True)
    finish = models.DateTimeField(default=None, null=True)
    is_active = models.BooleanField(default=True)


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)


class ProductSale(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, "sales")
    sportsman = models.ForeignKey(
        "users.User", models.CASCADE, "sportsman_purchases", null=True, blank=True
    )
    trainer = models.ForeignKey(
        "users.User", models.CASCADE, "trainer_purchases", null=True, blank=True
    )


class SubscriptionSale(models.Model):
    tarif = models.ForeignKey(Tarif, models.CASCADE, "sales")
    sportsman = models.ForeignKey(
        "users.User", models.CASCADE, "sportsman_subscriptions", null=True, blank=True
    )
    trainer = models.ForeignKey(
        "users.User", models.CASCADE, "trainer_subscriptions", null=True, blank=True
    )
    count = models.IntegerField(default=1)
