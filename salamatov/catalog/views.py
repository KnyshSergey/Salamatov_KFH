from django.shortcuts import render
from django.views.generic import TemplateView


class BaseView(TemplateView):
    template_name = "base.html"

    def get(self, request):
        return render(request, self.template_name)


class CatalogView(TemplateView):
    template_name = "catalog/catalog.html"

    def get(self, request):
        return render(request, self.template_name)
