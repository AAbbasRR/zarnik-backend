from django.contrib.auth import views
from django.urls import path
from django.views.generic.base import TemplateView

app_name = 'login'
urlpatterns = [
    path('', views.LoginView.as_view(template_name="login/login.html"), name='login'),
]
