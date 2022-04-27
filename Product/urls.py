from django.urls import path
from .views import Productviewall, ProductsUpdate

app_name = 'product'
urlpatterns = [
    path('product_list/', Productviewall, name="product_list"),
    path('product_edit/<int:pk>', ProductsUpdate.as_view(), name="product_edit"),
]
