from django.shortcuts import render,redirect
from home.views import *
from .models import Customer
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Customer.objects.get(username=username)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'signin.html')
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_password = request.POST.get('confirm_password')
        if c_password == password:
            user=Customer.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('signin')
    return render(request, 'signup.html')