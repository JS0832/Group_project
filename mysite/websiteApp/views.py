"""Views within Django structure, each function returns a HTML render
of a website page"""
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
import websiteApp.lib.websiteApp.codebase as gameBase
from .models import *

def index(request):
    """Invoke to return HTML render of index page"""
    # Render simply returns the html, add contect for personalised changes
    return render(request, 'websiteApp/login.html')

def login(request):
    """Invoke to return HTML render of login page"""
    context = {}
    if request.method == 'POST':
        #print(pretty_request(request)) #DEBUG COMMAND: DO NOT INCLUDE WHILE LIVE!
        given_username = request.POST.get('username')
        given_password = request.POST.get('password')
        user = authenticate(email=given_username, password=given_password)
        if user is not None:
            request.session['username']= user.username
            request.session['logged_in'] = True
        else:
            context['invalid_login'] = True

    context['logged_in'] = request.session.get('logged_in', False)
    return render(request, 'websiteApp/login.html', context)

def register(request):
    """Invoke to return HTML render of register page"""
    context = {}

    if request.method == 'POST':
        #print(pretty_request(request)) #DEBUG COMMAND: DO NOT INCLUDE WHILE LIVE!
        password_a = request.POST.get('password1')
        password_b = request.POST.get('password2')

        if password_a == password_b:
            given_username = request.POST.get('username')
            given_email = request.POST.get('email')
            try:
                user = User.objects.create_user(
                                            username=given_username,
                                            email=given_email,
                                            password=password_a,
                                            )
                user.save()
                request.session['username'] = user.username
                request.session['logged_in'] = True

            except IntegrityError:
                context['not_available'] = True

        else:
            context['password_not_same'] = True

    context['logged_in'] = request.session.get('logged_in', False)
    return render(request, 'websiteApp/register.html', context)

def game(request):
    """Invoke to return HTML render of game page"""
    riddle = Riddle.objects.order_by('pk')[0]
        # Just picks the first one, TODO: change daily
    not_done_riddle = True
    answer_wrong = False
    riddle_text = riddle.question

    if request.method == 'POST':
        #print(pretty_request(request)) #DEBUG COMMAND: DO NOT INCLUDE WHILE LIVE!
        response = request.POST.get('answer')
        if gameBase.riddleCheck(riddle, response):
            not_done_riddle = False
        else:
            answer_wrong = True

    context = {
        'not_done_riddle': not_done_riddle,
        'answer_wrong': answer_wrong,
        'riddle_text': riddle_text,
    }
    return render(request, 'websiteApp/game.html', context)

def location(request):
    """Invoke to return HTML render of location page"""
    return render(request, 'websiteApp/location.html')

def campus_exploration(request):
    """Invoke to return HTML render of campus ecploration page"""
    return render(request, 'websiteApp/campus_exploration.html')

def main(request):
    """Invoke to return HTML render of main page"""
    return render(request, 'websiteApp/main.html')

def settings(request):
    """Invoke to return HTML render of settings page"""
    return HttpResponse(request, "Settings TODO")

def introduce(request):
    """Invoke to return HTML render of introduction page"""
    return HttpResponse(request, "Introduction TODO")

#DEBUG FUNCTION

# https://gist.github.com/defrex/6140951
def pretty_request(request):
    """Turns the HTTP request into a readable string

    Paramters:
    request : HTTP Request"""
    headers = ''
    for header, value in request.META.items():
        if not header.startswith('HTTP'):
            continue
        header = '-'.join([h.capitalize() for h in header[5:].lower().split('_')])
        headers += '{}: {}\n'.format(header, value)

    return (
        '{method} HTTP/1.1\n'
        'Content-Length: {content_length}\n'
        'Content-Type: {content_type}\n'
        '{headers}\n\n'
        '{body}'
    ).format(
        method=request.method,
        content_length=request.META['CONTENT_LENGTH'],
        content_type=request.META['CONTENT_TYPE'],
        headers=headers,
        body=request.body,
    )
