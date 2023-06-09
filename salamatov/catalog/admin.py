from django.contrib import admin
from .models import Category, Good, Certificate

@admin.register(Good)
class WoodAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "date_of_manufacture", "price", "amount", "category", "photo")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "photo")

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "photo")
