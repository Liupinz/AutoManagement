from django.shortcuts import render, redirect
from django.http import HttpResponse
from dams.models import User
from AutoManagement.settings import BASE_DIR
import os
import json

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

def mchoice(request):
    return render(request, 'dams/mchoice.html')

def mysql(request):
    return render(request, 'dams/mysql.html')

def singlemysql(request):
    ip = request.POST.get('hostip')
    password = request.POST.get('mpassword')
    inventory_path = os.path.join(BASE_DIR, 'ansibleAuto/mysql/inventory/hosts')
    info_dict = ip + " " + "ansible_connection=ssh" + " " + "ansible_user=root" + " " + "ansible_host="+ ip + " " + "ansible_ssh_pass=" + password
    with open(inventory_path, 'w') as f:
        f.write(info_dict)

    return HttpResponse("ok")









