from django.views.generic import ListView, DetailView

from apps.shop.models import Product


class HomeView(ListView):
    template_name = "shop/home.html"
    model = Product
    context_object_name = "products"
    paginate_by = 6


class ProductDetailView(DetailView):
    template_name = "shop/product_detail.html"
    model = Product
    context_object_name = "product"
