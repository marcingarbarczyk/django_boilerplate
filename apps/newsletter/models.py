from django.db import models
from django_extensions.db.models import TimeStampedModel, ActivatorModel
from django.utils.translation import gettext as _

from apps.newsletter.managers import ActiveSubscribersManager


class Subscriber(TimeStampedModel, ActivatorModel):
    email = models.EmailField()
    objects = models.Manager()
    active_subscribers = ActiveSubscribersManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("Subscriber")
        verbose_name_plural = _("Subscribers")
