from django.urls import path

from apps.blog.views import BlogView, PostDetailView, BlogCategoryView

app_name = "blog"

urlpatterns = [
    path("", BlogView.as_view(), name="blog"),
    path("category/<slug:slug>/", BlogCategoryView.as_view(), name="blog-category"),
    path("<slug:slug>", PostDetailView.as_view(), name="post-detail"),
]
