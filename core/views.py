from django.shortcuts import render
from core.models import *

def home(request):
    blog = Blog.objects.order_by("-id")
    partners = Partner.objects.order_by("-id")
    context = {
        'blog': blog,
        'partners': partners,
    }
    return render(request, 'index.html', context)