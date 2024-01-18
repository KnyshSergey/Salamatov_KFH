from django.shortcuts import redirect
from .models import Cart
from catalog.models import Good
from django.views.generic import RedirectView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class CartView(RedirectView):

    def get(self, request):
        return redirect('catalog')

    @method_decorator(login_required())
    def post(self, request):
        good = Good.objects.get(id=request.POST['good_id'])
        cart = Cart.objects.get(user=request.user)
        cart.products.add(good)

        return redirect('catalog')

class CartRemove(RedirectView):
    template_name = ""

    def get(self, request):
        return redirect('catalog.html')

    @method_decorator(login_required)
    def post(self, request):
        good = Good.objects.get(id=request.POST['good_id'])
        cart = Cart.objects.get(user=request.user)
        cart.products.remove(good)

        return redirect('catalog')