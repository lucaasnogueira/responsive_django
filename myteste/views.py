from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def home (request):
    return render ( request, 'index.html')

def welcome (request):
    return render(request, 'welcome.html')

def login(request):
    return render(request, 'login.html')
