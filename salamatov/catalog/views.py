from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Good, Category
from django.db.models import Q

class BaseView(TemplateView):
    template_name = "base.html"

    def get(self, request):


        return render(request, self.template_name)


class CatalogView(TemplateView):
    template_name = "catalog/catalog.html"

    def get(self, request):
        good = Good.objects.all()
        categories = Category.objects.all()

        params = {
            'goods': good,
            'categories': categories
        }
        return render(request, self.template_name, params)


class GoodView(TemplateView):
    template_name = "catalog/good.html"


    def get(self, request, id):
        good = Good.objects.get(id=id)
        category = Category.objects.all()
        categories = Category.objects.all()

        params = {
            'good': good,
            'category': category,
            'categories': categories
        }
        return render(request, self.template_name, params)


class SearchView(TemplateView):
    template_name = "catalog/catalog.html"

    def post(self, request):
        search = request.POST['search']
        good_by_name = Good.objects.filter(Q(name__icontains=search) | Q(description__icontains=search) | Q(price__icontains=search))
        categories = Category.objects.all()

        params = {
            'goods': good_by_name,
            'categories': categories
        }

        return render(request, self.template_name, params)

class CategoryCatalogView(TemplateView):
    template_name = "catalog/catalog.html"

    def get(self, request, id):
        category = Category.objects.get(id=id)
        goods = Good.objects.filter(category=category)
        categories = Category.objects.all()

        params = {

            'categories': categories,
            'goods': goods,

        }

        return render(request, self.template_name, params)
