from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.membership.managers import UserManager
from django.utils.translation import gettext as _


class User(AbstractUser):
    username = None
    objects = UserManager()
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
