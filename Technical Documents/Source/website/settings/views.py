from django.shortcuts import render

from django.template.loader import get_template
from django.http import HttpResponse

def settings(request):
    template = get_template('settings.html')
    return HttpResponse(template.render())

def home(request):
    template = get_template('home.html')
    return HttpResponse(template.render())

def login(request):
    template = get_template('login.html')
    return HttpResponse(template.render())
