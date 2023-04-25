from django.shortcuts import render

from django.template.loader import get_template
from django.http import HttpResponse

def resources(request):
    template = get_template('resources.html')
    return HttpResponse(template.render())
