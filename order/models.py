from datetime import datetime


from django.db import models

from product.models import Product
from customer.models import  User
import secrets


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


class Gift_Cart(models.Model):
    @staticmethod
    def random_str():
        upper_alpha = "ABCDEFGHJKLMNPQRSTVWXYZ"
        # Create an 8 char random string from our alphabet
        random_str = "".join(secrets.choice(upper_alpha) for i in range(8))
        return random_str

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(default=random_str.__func__, max_length=10)
    date = models.DateField()

    def check_date(self):
        date = datetime.now()
        return date > self.date
