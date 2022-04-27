from django.urls import reverse_lazy

from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import DeleteView

from .models import Slider, Sections


class SliderCreate(LoginRequiredMixin, CreateView):
    model = Slider
    fields = '__all__'
    success_url = reverse_lazy("section:Sliderlist")
    template_name = 'section/slider_create_update.html'


class SliderUpdate(LoginRequiredMixin, UpdateView):
    model = Slider
    fields = '__all__'
    success_url = reverse_lazy("section:Sliderlist")
    template_name = 'section/slider_create_update.html'


class SliderDelete(LoginRequiredMixin, DeleteView):
    model = Slider
    success_url = reverse_lazy("section:Sliderlist")
    template_name = 'section/slider_delete.html'


@login_required
def sliderviewall(request):
    context = {
        "slider_data": Slider.objects.all(),
    }
    return render(request, 'section/slider_list.html', context)


class SectionUpdate(LoginRequiredMixin, UpdateView):
    model = Sections
    fields = ["title", "subtitle", "content"]
    success_url = reverse_lazy("section:Sectionlist")
    template_name = 'section/section_update.html'


@login_required
def sectionviewall(request):
    context = {
        "section_data": Sections.objects.all(),
    }
    return render(request, 'section/section_list.html', context)
