# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

# class User(AbstractUser):
#     class Meta(AbstractUser.Meta):
#         pass


class User(AbstractUser):
    TRENER = "trener"
    SPORTSMEN = "sportsmen"
    ADMIN_GROUP = "admin_group"
    ADMIN = "admin"
    ROLE_CHOICES = [
        (TRENER, "trener"),
        (SPORTSMEN, "sportsmen"),
        (ADMIN_GROUP, "admin_group"),
        (ADMIN, "Admin"),
    ]
    username = models.CharField(
        max_length=150,
        blank=False,
        unique=True,
        validators=[RegexValidator(regex=r"^[\w.@+-]+$")],
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
    )
    email = models.EmailField(max_length=254, blank=False, unique=True)
    phone = models.CharField(max_length=254, blank=False, default=None, null=True)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=TRENER,
    )

    class Meta(AbstractUser.Meta):
        ordering = ["username"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

    @property
    def is_trener(self):
        return self.role == self.TRENER

    @property
    def is_sportsmen(self):
        return self.role == self.SPORTSMEN

    @property
    def is_admin_group(self):
        return self.role == self.ADMIN_GROUP

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def balance(self):
        # return sum(self.order_set.all().values_list("amount", flat=True))
        return sum(
            self.order_set.filter(status="SUCCESS").values_list("sum", flat=True)
        )

    @property
    def debit(self):
        # return sum(self.order_set.all().values_list("amount", flat=True))
        return sum(
            self.order_set.filter(status="SUCCESS").values_list("sum", flat=True)
        ) - sum(self.debit_set.filter(status="SUCCESS").values_list("sum", flat=True))


class Group(models.Model):
    groupname = models.CharField(max_length=150, blank=True, unique=True)
    trainer = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="adminisration_groups"
    )
    # sportsmen = models.ManyToManyField(
    #     "users.User", on_delete=models.PROTECT, related_name="pet"
    # )
    # date_creation = models.DateTimeField(auto_now_add=True)


class GroupMember(models.Model):
    group = models.ForeignKey(Group, models.PROTECT, "members")
    sportsman = models.OneToOneField(
        "users.User", on_delete=models.PROTECT, related_name="group"
    )
