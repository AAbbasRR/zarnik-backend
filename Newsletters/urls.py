from django.urls import path
from .views import *

app_name = 'newsletters'
urlpatterns = [
    path('list/', newsletterviewall, name="NewSletterlist"),
]
