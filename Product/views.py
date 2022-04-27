from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Products


class ProductsUpdate(LoginRequiredMixin, UpdateView):
    model = Products
    fields = ["subtitle", "content", "ProductSize", "ProductWeight", "ProductQuality", "MotherPacking", "ProductWhoSell"]
    success_url = reverse_lazy("product:product_list")
    template_name = 'product/product_update.html'


@login_required
def Productviewall(request):
    context = {
        "Products_data": Products.objects.all(),
    }
    return render(request, 'product/product_list.html', context)
