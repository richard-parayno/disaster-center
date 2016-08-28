from django.shortcuts import render,redirect
from disaster_center.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")


def floods(request):
    return render(request, "floods.html")

def storms(request):
    return render(request, "storms.html")

def updates(request):
    return render(request, "updates.html")

def traffic(request):
    return render(request, "traffic.html")

def danger_zones(request):
    return render(request, "danger-zones.html")

def new_user(request):
    return render(request, "new-user.html")

def login(request):
    return render(request, "login.html")

def new_user_account(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POS['first_name']
        last_name = request.POST['last_name']
        user = User.objects.createUser(email = email, password = password)
        user.first_name = first_name
        user.last_name = last_name
        #messages.error(request, 'Hello WOrld')
        user.save()
    return redirect('index')

def login_account(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email = email, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('danger_zones')

    else:
        return render(request, 'index')

def logout_account(request):
    logout(request, user)
    return redirect('index')
