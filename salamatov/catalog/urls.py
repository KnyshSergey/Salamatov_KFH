from django.contrib import admin
from django.urls import path
from .views import CatalogView, BaseView, GoodView, SearchView, CategoryCatalogView


urlpatterns = [
    path("", BaseView.as_view(), name="base"),
    path("catalog/", CatalogView.as_view(), name="catalog"),
    path("catalog/good/<int:id>", GoodView.as_view(), name="catalog-good"),
    path('categories/category-<int:id>/', CategoryCatalogView.as_view(), name="catalog-category"),
    path("catalog/search/", SearchView.as_view(), name="catalog-search")
]
