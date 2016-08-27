from django.shortcuts import render
from disaster_center.models import *

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

def dangerzones(request):
    return render(request, "danger-zones.html")

def newuser(request):
    return render(request, "new-user.html")

def login(request):
    return render(request, "login.html")
