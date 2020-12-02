from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def show(request):
    return HttpResponse("Show method")

def random(request, name):
    return HttpResponse(f"Hello {name.capitalize()}")