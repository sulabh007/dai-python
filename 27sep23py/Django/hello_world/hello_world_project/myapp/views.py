from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")

def welcome(request):
    return HttpResponse("Welcome to django prongramming")

def factorial(request):
    return HttpResponse("In Factorial")