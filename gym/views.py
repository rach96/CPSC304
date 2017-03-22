from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db import connection

from gym.query import my_custom_sql

def viewC(request):
    data = my_custom_sql(request)
    print(data)
    return render(request, 'gym/viewC.html', data)
# this is where we link the html to our app. where we put REST


def index(request):
    return HttpResponse("Hello, world. You're at the Awesome Gym.")

