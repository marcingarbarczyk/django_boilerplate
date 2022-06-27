from django.db import models
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel, ActivatorModel
from django.utils.translation import gettext as _


class Category(TitleSlugDescriptionModel):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Post(TitleSlugDescriptionModel, TimeStampedModel, ActivatorModel):
    categories = models.ManyToManyField(Category, related_name="posts")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
