from time import sleep

from django.conf import settings
from django.core.mail import send_mail

from apps.newsletter.models import Subscriber
from project.celery import app


@app.task
def send_newsletter(ids):
    subscribers = Subscriber.objects.filter(id__in=ids)
    for subscriber in subscribers:
        print("Sending newsletter...")

        send_mail(
            subject="Newsletter subject",
            message="Newsletter message",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[subscriber.email],
            fail_silently=False,
        )
    sleep(10)
