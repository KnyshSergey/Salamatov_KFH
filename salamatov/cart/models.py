from django.db import models
from catalog.models import Good
from django.contrib.auth.models import User



class Cart(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="cart")
    products = models.ManyToManyField(Good, blank=True)

    def get_total_price(self):
        return sum([good.price for good in self.products.all()])

    def get_total_quantity(self):
        return len([good for good in self.products.all()])

    def display_products(self):
        return ", ".join([good.name for good in self.products.all()])

