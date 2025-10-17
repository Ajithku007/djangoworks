from http.client import HTTPResponse
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def Home(request):
    return HttpResponse("welcome to django application")

def Index(request):
    return HttpResponse("Welcome to index page")