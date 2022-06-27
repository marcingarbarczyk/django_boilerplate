from apps.blog.urls_api import router
from apps.shop.views_api import ProductViewSet

router.register(r"products", ProductViewSet)
urlpatterns = router.urls
