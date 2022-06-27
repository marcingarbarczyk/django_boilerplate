from django.views.generic import TemplateView

from apps.newsletter.models import Subscriber
from apps.newsletter.tasks import send_newsletter


class SendNewsletterView(TemplateView):
    template_name = "newsletter/newsletter_async.html"

    def get(self, request, *args, **kwargs):
        subscribers = list(Subscriber.active_subscribers.values_list("id", flat=True))
        send_newsletter.delay(subscribers)
        return super().get(request, *args, **kwargs)
