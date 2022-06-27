from django.urls import path

from apps.newsletter.views import SendNewsletterView

app_name = "newsletter"

urlpatterns = [
    path("", SendNewsletterView.as_view(), name="send-newsletter"),
]
