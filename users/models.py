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