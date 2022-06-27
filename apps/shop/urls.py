from django.urls import path

from apps.shop.views import HomeView, ProductDetailView

app_name = "shop"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("<slug:slug>", ProductDetailView.as_view(), name="product-detail"),
]
