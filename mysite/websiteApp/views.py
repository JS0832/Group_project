from django.http import HttpResponse
from django.shortcuts import redirect, render
import websiteApp.lib.websiteApp.codebase as gameBase
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def index(request):
    # Render simply returns the html, add contect for personalised changes
    return render(request, 'websiteApp/login.html')

def login(request):

    #Obtains information from login page
    if request.method == "POST":
        username = request.POST.get("AccountNumber")
        password = request.POST.get("Password")

        #authenticate user against existing login credentials
        user = authenticate(username="AccountNumber", password="Password")

        #If the login exists, logs in. Sends user to game.html
        if user is not None: 
            login(request, user)
            return render (request, 'websiteApp/game.html')

        #Else, posts a error message and redirects the user to the login page once again
        else:
            messages.error(request, "Bad Credentials")
            return redirect ("login")

    return render(request, 'websiteApp/login.html')

def register(request):
    #Taking the post method of the registration
    if request.method == "POST":
        email = request.POST.get("RegisteredAccountNumber")
        username = request.POST.get("RegisteredUsername")
        password = request.POST.get("RegisteredPassword")
        password_repeat = request.POST.get("RegisteredPassword1")

        #Creating the user object
        #Need to save to database
        #myuser = User.objects.create_user(username=username, email=email, password=password)
        #myuser.save()
        
        #Temporary success message, subject to change
        messages.success(request, "Your account has successfully been created.")

        return redirect("login")

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