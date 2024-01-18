from django.contrib import admin
from .models import News

@admin.register(News)
class CartNews(admin.ModelAdmin):
    list_display = ['title', 'description', 'created']
