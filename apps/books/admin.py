from django.contrib import admin

from apps.books.models import Author, Store, Book, Publisher


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "age",
    )
    search_fields = ("name",)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "pages",
        "price",
        "rating",
        "publisher",
        "pubdate",
    )
    search_fields = ("name",)


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("name",)
