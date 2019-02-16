from django.shortcuts import render, redirect
from django.http import HttpResponse
from dams.models import User

# Create your views here.

def login(request):
    return render(request, 'dams/login.html')

def logincheck(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    userResult = User.objects.filter(uname=username, upassword=password)
    if (len(username) > 0):
        return redirect('/dashboard')
    else:
        return redirect('/login')

def dashboard(request):
    return render(request, 'dams/dashboard.html')











