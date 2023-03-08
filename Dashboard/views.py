from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'Dashboard/home.html')

def login(request):
    return render(request, 'Dashboard/login.html')

def register(request):
    return render(request, 'Dashboard/register.html')