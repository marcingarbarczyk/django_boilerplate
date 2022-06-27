from django.core.management.base import BaseCommand
import random
from django.contrib.auth import get_user_model
from django_seed import Seed
from apps.shop.models import *
from apps.blog.models import *
from apps.books.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):

        seeder = Seed.seeder()

        # clear all data (if you want of course)

        Product.objects.all().delete()
        Order.objects.all().delete()
        OrderItem.objects.all().delete()
        Category.objects.all().delete()
        Post.objects.all().delete()
        Publisher.objects.all().delete()
        Author.objects.all().delete()
        Book.objects.all().delete()
        Store.objects.all().delete()

        # Member ship app

        seeder.add_entity(
            get_user_model(),
            1000,
            {
                "first_name": lambda x: seeder.faker.first_name(),
                "last_name": lambda x: seeder.faker.last_name(),
                "email": lambda x: seeder.faker.email(),
            },
        )

        # Shop app

        seeder.add_entity(
            Category,
            30,
            {
                "title": lambda x: seeder.faker.text(20),
                "description": lambda x: seeder.faker.text(),
            },
        )

        seeder.add_entity(
            DeliveryAddress,
            230,
            {
                "address": lambda x: seeder.faker.address(),
                "city": lambda x: seeder.faker.city(),
                "state": lambda x: seeder.faker.state_abbr(),
                "zip_code": lambda x: seeder.faker.zipcode(),
            },
        )

        seeder.add_entity(
            Product,
            250,
            {
                "title": lambda x: seeder.faker.text(20),
                "description": lambda x: seeder.faker.text(),
                "price": lambda x: random.randint(30, 300),
                "image": lambda x: seeder.faker.image_url(),
                "created_at": lambda x: seeder.faker.date_time(),
                "updated_at": lambda x: seeder.faker.date_time(),
            },
        )

        seeder.add_entity(
            ProductVote,
            2550,
            {
                "vote": lambda x: random.randint(1, 5),
            },
        )

        seeder.add_entity(
            Order,
            5030,
            {
                "name": lambda x: seeder.faker.name(),
                "address": lambda x: seeder.faker.address(),
                "city": lambda x: seeder.faker.city(),
                "state": lambda x: seeder.faker.state_abbr(),
                "zip_code": lambda x: seeder.faker.zipcode(),
                "total": lambda x: random.randint(100, 5000),
                "created_at": lambda x: seeder.faker.date_time(),
                "updated_at": lambda x: seeder.faker.date_time(),
            },
        )

        seeder.add_entity(
            OrderItem,
            10200,
            {
                "quantity": lambda x: random.randint(5, 15),
                "price": lambda x: random.randint(100, 500),
            },
        )

        # Blog app

        seeder.add_entity(
            Category,
            15,
            {
                "title": lambda x: seeder.faker.text(5),
                "description": lambda x: seeder.faker.text(),
            },
        )

        seeder.add_entity(
            Post,
            215,
            {
                "title": lambda x: seeder.faker.text(),
                "description": lambda x: seeder.faker.text(),
            },
        )

        seeder.add_entity(
            Comment,
            215,
            {
                "author": lambda x: seeder.faker.name(),
                "text": lambda x: seeder.faker.text(),
            },
        )

        # Books app

        seeder.add_entity(
            Publisher,
            100,
            {
                "name": lambda x: seeder.faker.company(),
            },
        )

        seeder.add_entity(
            Author,
            500,
            {
                "name": lambda x: seeder.faker.name(),
                "age": lambda x: random.randint(20, 80),
            },
        )

        seeder.add_entity(
            Book,
            10000,
            {
                "name": lambda x: seeder.faker.company(),
                "pages": lambda x: random.randint(100, 500),
                "price": lambda x: random.randint(100, 500),
                "rating": lambda x: random.randint(1, 5),
                "pubdate": lambda x: seeder.faker.date_time(),
            },
        )

        seeder.add_entity(
            Store,
            100,
            {
                "name": lambda x: seeder.faker.text(15),
            },
        )

        seeder.execute()
