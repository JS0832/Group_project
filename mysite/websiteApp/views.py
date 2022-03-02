from django.http import HttpResponse
from django.shortcuts import render
import websiteApp.lib.websiteApp.codebase as gameBase

def index(request):
    # Render simply returns the html, add contect for personalised changes
    return render(request, 'websiteApp/login.html')

def login(request):
    return render(request, 'websiteApp/login.html')

def register(request):
    return render(request, 'websiteApp/register.html')

def game(request):
    return render(request, 'websiteApp/game.html')

def location(request):
    return render(request, 'websiteApp/location.html')

def campus_exploration(request):
    return render(request, 'websiteApp/campus_exploration.html')

def main(request):
    return render(request, 'websiteApp/main.html')

def settings(request):
    return HttpResponse(request, "Settings TODO")

def introduce(request):
    return HttpResponse(request, "Introduction TODO")