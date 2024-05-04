from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255, null=True)
    registration_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Клиент: {self.name}, email: {self.email}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return f"Товар: {self.name}, Цена: {self.price}"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(default=timezone.now)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)

    def __str__(self):
        return f"Заказ {self.id} от {self.date.strftime('%d-%m-%Y')}: {self.product.name} Кол-во: {self.quantity}"

    def save(self, *args, **kwargs):
        self.total_sum = self.quantity * self.product.price
        super(Order, self).save(*args, **kwargs)
