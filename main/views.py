from django.shortcuts import render
from .models import *

def home(request):
    Categories = category.objects.all()
    Services = services.objects.all()
    context = {
        'Categories':Categories,
        'Services':Services,
    }

    return render(request, 'index.html', context)