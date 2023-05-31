from django.db import models


class Category(models.Model):
    name = models.TextField()
    photo = models.ImageField(upload_to="category-images/")
    description = models.TextField(200)

    def __str__(self):
        return self.name

class Wood(models.Model):
    name = models.TextField()
    description = models.TextField()
    date_of_manufacture = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, blank=False, max_digits=10)
    amount = models.IntegerField(blank=True, null=True)
    photo = models.ImageField("wood-images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


class Certificate(models.Model):
    name = models.TextField()
    description = models.TextField()
    photo = models.ImageField("certificates/")
