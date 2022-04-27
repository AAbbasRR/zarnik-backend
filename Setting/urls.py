from django.urls import path
from .views import *

app_name = 'setting'
urlpatterns = [
    path('Setting/', settingviewall, name="Settinglist"),
    path('Setting/update/<int:pk>', SettingUpdate.as_view(), name="SettingUpdate"),
]
