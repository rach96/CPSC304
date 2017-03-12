from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# this is where we link the html to our app. where we put REST
def index(request):
    return HttpResponse("Hello, world. You're at the Awesome Gym.")