from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from random import choice, randint, uniform
from marketapp.models import Client, Product, Order


class Command(BaseCommand):
    help = "Заполняет БД фейковыми записями для проверки"

    def handle(self, *args, **options):
        self.stdout.write("Начинаем заполнение базы данных...")

        # Создаем клиентов
        clients = [
            Client.objects.create(
                name=f"Name{i} Lastname{i}",
                email=f"name{i}@example.com",
                phone_number=f"120{i}456{i}",
                address=f"Some Strit, {i}",
                registration_date=timezone.now()
            ) for i in range(1, 11)
        ]

        # Создаем товары
        products = [
            Product.objects.create(
                name=f"Product{i}",
                description="...",
                price=uniform(100.0, 5000.0),
                quantity=randint(20, 100),
                date_added=timezone.now() - timedelta(days=365)
            ) for i in range(1, 31)
        ]

        # Создаем заказы
        for _ in range(300):
            order = Order.objects.create(
                client=choice(clients),
                product=choice(products),
                quantity=randint(1, 5),
                date=timezone.now() - timedelta(days=randint(1, 360))
            )

        self.stdout.write(self.style.SUCCESS('База успешно заполнена случайными данными'))