from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth.decorators import login_required


from gym.query import my_custom_sql

def index(request):
    return HttpResponse("Hello, world. You're at the Awesome Gym.")

def page1(request):
    return HttpResponse("This is where the aggregations will go")

def page2(request):
    return HttpResponse("This is where the projections will go")

#testPage
def viewC(request):
    data = my_custom_sql(request)
    print(data)
    return render(request, 'gym/viewC.html', data)
# this is where we link the html to our app. where we put REST

@login_required
def page3(request):
    return HttpResponse("This is where we can delete tuples in clean room")

@login_required
def page4(request):
    return HttpResponse("This is where we can update items OR delete items so that there is a cascade")


