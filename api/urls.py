from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    path("products/", ProductsListView.as_view(), name='product_list'),
    path("themeSettings/", ThemeSettingListView.as_view(), name='themeSettings_list'),
    path("section/", SectionListView.as_view(), name='section_list'),
    path("slider/", SliderListView.as_view(), name='slider_list'),
    path("newsletter/", NewSletterCreateView.as_view(), name='NewSletter_Create'),
]
