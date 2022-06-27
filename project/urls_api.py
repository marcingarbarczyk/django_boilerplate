from django.urls import path, include
from rest_framework import routers

app_name = "api"
router = routers.DefaultRouter()
router.registry.extend(include("apps.shop.urls_api"))
router.registry.extend(include("apps.shop.urls_api"))

urlpatterns = [
    path("", include(router.urls)),
]
