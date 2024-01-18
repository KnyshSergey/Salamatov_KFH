from django.db import models

class News(models.Model):

    title = models.TextField(max_length=100)
    description = models.TextField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    photo = models.ImageField(upload_to="news-images/", default="placeholder.jpg")

    def __str__(self):
        return self.title

