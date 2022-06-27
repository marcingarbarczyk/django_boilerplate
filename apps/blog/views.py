from django.db.models import Count
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from apps.blog.forms import CommentForm
from apps.blog.models import Post, Category, Comment


class BlogView(ListView):
    template_name = "blog/blog.html"
    model = Post
    context_object_name = "posts"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.annotate(posts_count=Count("posts")).filter(posts_count__gt=0)
        return context


class BlogCategoryView(BlogView):
    template_name = "blog/blog_category.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(categories__slug=self.kwargs["slug"])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get(slug=self.kwargs["slug"])
        return context


class PostDetailView(FormMixin, DetailView):
    template_name = "blog/post_detail.html"
    model = Post
    context_object_name = "post"
    form_class = CommentForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"slug": self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(post=self.get_object()).order_by("-created")
        context["form"] = CommentForm(initial={"post": self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
