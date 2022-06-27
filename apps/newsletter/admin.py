from django.contrib import admin
from django.utils.translation import gettext as _


from apps.newsletter.models import Subscriber
from apps.newsletter.tasks import send_newsletter


def send_newsletter_async(modeladmin, request, queryset):
    ids = queryset.values_list("id", flat=True)
    send_newsletter.delay(ids)


send_newsletter.short_description = _("Send newsletter (async)")


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "status", "activate_date", "deactivate_date")
    list_filter = ("status",)
    search_fields = ("email",)
    actions = [send_newsletter_async]
