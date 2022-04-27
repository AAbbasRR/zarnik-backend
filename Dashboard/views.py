from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import TemplateView

from Login.models import User


class Dashboard(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'dashboard/index.html'
    success_url = reverse_lazy("dashboard:index")

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)


class PasswordChange(LoginRequiredMixin, PasswordChangeView, TemplateView):
    template_name = "dashboard/password_change_form.html"
    success_url = reverse_lazy("dashboard:password_change_done")
