from django.shortcuts import render
from disaster_center.model import *

# Create your views here.
def index(request):
    return render(request, "index.html")
