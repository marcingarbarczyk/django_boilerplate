from apps.blog.views_api import PostViewSet, CategoryViewSet
from project.urls_api import router

router.register(r"posts", PostViewSet)
router.register(r"categories", CategoryViewSet)
urlpatterns = router.urls
