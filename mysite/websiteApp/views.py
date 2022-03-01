from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("TODO, SYNC HTTP RESPONSE TO INDEX HTML")

def login(request):
    return HttpResponse("TODO, SYNC HTTP RESPONSE TO LOGIN HTML")

def register(request):
    return HttpResponse("TODO, SYNC HTTP RESPONSE TO REGISTER HTML")
