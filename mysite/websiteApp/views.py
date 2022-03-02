from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # Render simply returns the html, add contect for personalised changes
    # Addded comment
    return render(request, 'websiteApp/login.html')

def login(request):
    return render(request, 'websiteApp/login.html')

def register(request):
    return render(request, 'websiteApp/register.html')
