from django.shortcuts import render, redirect
from django.contrib import messages
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
    Categories = category.objects.all()
    Services = services.objects.all()
    Service = services.objects.get(id = id)
    images = serviceImages.objects.filter(service = Service)
    context = {
        'Service':Service,
        'images':images,
        'Categories':Categories,
        'Services':Services,
    }
    return render(request, 'product-detail.html', context)

def CheckOut(request, id):
    Categories = category.objects.all()
    Services = services.objects.all()
    Service = services.objects.get(id = id)
    current_user = request.user
    user_profile = profile.objects.get(user = current_user)
    status = False
    price = Service.price
    dicount = (price*30)/100
    dicounted_price = price-dicount
    if user_profile.is_employee:
        status = True
        dicount = (price*40)/100
        dicounted_price = price-dicount
    if request.method == 'POST':
        notes = request.POST.get('notes')
        date = request.POST.get('date')
        time = request.POST.get('time')
        place_oder = order.objects.create(
            profile = user_profile, 
            service = Service,
            status = 'pending',
            note = notes,
            date = date,
            time = time
        )
        place_oder.save()
        messages.success(request, "Order hase been placed successfully!")
        return redirect('CheckOut', id)

    context = {
        'Service':Service,
        'status':status,
        'dicounted_price':dicounted_price,
        'Categories':Categories,
        'Services':Services,
    }
    return render(request, 'checkout.html', context)



