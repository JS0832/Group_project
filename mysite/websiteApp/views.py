from django.http import HttpResponse
from django.shortcuts import render
from .models import Riddles
import websiteApp.lib.websiteApp.codebase as gameBase

def index(request):
    # Render simply returns the html, add contect for personalised changes
    return render(request, 'websiteApp/login.html')

def login(request):
    return render(request, 'websiteApp/login.html')

def register(request):
    return render(request, 'websiteApp/register.html')

def game(request):
    riddle = Riddles.objects.order_by('pk')[0]
    not_done_riddle = True
    answer_wrong = False
    riddle_text = riddle.question

    if request.method == 'POST':
        response = request.POST['answer']
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
    return render(request, 'websiteApp/location.html')

def campus_exploration(request):
    return render(request, 'websiteApp/campus_exploration.html')

def main(request):
    return render(request, 'websiteApp/main.html')

def settings(request):
    return HttpResponse(request, "Settings TODO")

def introduce(request):
    return HttpResponse(request, "Introduction TODO")