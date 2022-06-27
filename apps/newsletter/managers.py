from django.db import models


class ActiveSubscribersManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(deactivate_date__isnull=True, activate_date__isnull=False, status=self.model.ACTIVE_STATUS)
        )
