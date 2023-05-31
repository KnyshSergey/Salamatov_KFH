from django.contrib import admin
from django.urls import path
from .views import CatalogView, BaseView


urlpatterns = [
    path("", BaseView.as_view(), name="base"),
    path("catalog/", CatalogView.as_view(), name="catalog")
]