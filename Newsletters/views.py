from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import NewSletter


@login_required
def newsletterviewall(request):
    context = {
        "newsletter_data": NewSletter.objects.all(),
    }
    return render(request, 'newsletter/newsletter_list.html', context)
