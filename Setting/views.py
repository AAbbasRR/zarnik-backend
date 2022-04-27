from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from .models import ThemeSetting


class SettingUpdate(LoginRequiredMixin, UpdateView):
    model = ThemeSetting
    fields = ["value"]
    success_url = reverse_lazy("setting:Settinglist")
    template_name = 'setting/setting_update.html'


@login_required
def settingviewall(request):
    context = {
        "setting_data": ThemeSetting.objects.all(),
    }
    return render(request, 'setting/setting_list.html', context)
