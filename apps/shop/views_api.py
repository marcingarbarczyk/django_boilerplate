from rest_framework import viewsets

from apps.shop.models import Product
from apps.shop.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
