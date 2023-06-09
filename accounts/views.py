from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from main.models import *

# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('user_login')
    return render(request, 'login.html')
 
def Userlogout(request):
    logout(request)
    return redirect('home')

def user_SignUp(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        email = request.POST.get('email')
        EmpPhone = request.POST.get('EmpPhone')
        EmpCNIC = request.POST.get('EmpCNIC')
        EmpAddress = request.POST.get('EmpAddress')
        status = request.POST.get('status')

        user = User.objects.create_user(
            first_name = fname,
            last_name = lname,
            email = email, 
            username = username, 
            password = pass1
        )
        user_porfile = profile.objects.create(
            user = user,
            CNIC = EmpCNIC,
            phone = EmpPhone,
            adress = EmpAddress,
        )
        if status == "employee":
            user_porfile.is_employee = True
        user_porfile.save()

        messages.success(request, "Registration successfull!")
        return redirect('user_login')        
    return render(request, 'Register.html')