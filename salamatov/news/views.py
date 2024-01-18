from django.shortcuts import render
from django.views.generic import TemplateView
from .models import News
from catalog.models import Category

class NewsView(TemplateView):

    template_name = "news/news.html"

    def get(self, request):

        new = News.objects.all()
        categories = Category.objects.all()

        params = {
            'news': new.order_by('-created'),
            'categories': categories
        }


        return render(request, self.template_name, params)

