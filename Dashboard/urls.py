from django.contrib.auth import views
from django.urls import path
from .views import Dashboard, PasswordChange

app_name = 'dashboard'
urlpatterns = [
    path('', Dashboard.as_view(), name='index'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(template_name="dashboard/password_change_done.html"), name='password_change_done'),
]
