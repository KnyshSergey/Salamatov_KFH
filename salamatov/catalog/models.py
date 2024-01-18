from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.TextField()
    photo = models.ImageField(upload_to="category-images/")
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_category_url(self):
        return reverse("catalog-category", args=[self.id])

class Good(models.Model):
    name = models.TextField()
    description = models.TextField()
    date_of_manufacture = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, blank=False, max_digits=10)
    amount = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to="good-images/", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def get_category(self):
        return ", ".join([category.name for category in self.category.all()])

    def get_good_url(self):
        return reverse("catalog-good", args=[self.id])


class Certificate(models.Model):
    name = models.TextField()
    description = models.TextField()
    photo = models.ImageField("certificates/")
