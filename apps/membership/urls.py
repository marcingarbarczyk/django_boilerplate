from django.urls import path, include

app_name = "membership"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
]
