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

def shop(request):
    Categories = category.objects.all()
    Services = services.objects.all()
    context = {
        'Categories':Categories,
        'Services':Services,
    }
    return render(request, 'product-list.html', context)
    
def CategoryFilter(request, id):
    Category = category.objects.get(id = id)
    Categories = category.objects.all()
    Services = services.objects.filter(service_ctg = Category)
    context = {
        'Categories':Categories,
        'Services':Services,
        'ctg_id':id,
    }
    return render(request, 'product-list.html', context)

def ServiceDetails(request, id):
    Service = services.objects.get(id = id)
    images = serviceImages.objects.filter(service = Service)
    context = {
        'Service':Service,
        'images':images,
    }
    return render(request, 'product-detail.html', context)

def CheckOut(request, id):
    Service = services.objects.get(id = id)
    context = {
        'Service':Service,
    }
    return render(request, 'checkout.html', context)



