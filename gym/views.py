# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpRequest
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext

from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import login as view_login
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views.generic.edit import CreateView
import json
from .forms import MyFormPage1
from .forms import MyFormPage2
from .forms import MyFormPage3
from .forms import MyFormPage4
from .forms import MyFormPage5


from gym.query import my_custom_sql,my_sql_query_1,my_sql_query_2,my_sql_query_7,my_sql_query_6,my_sql_query_5,my_sql_query_8,\
    my_sql_query_9,my_sql_query_10,my_sql_query_11,my_sql_query_12,my_sql_query_13,my_sql_query_14

def index(request):
    #my_custom_sql(request)
    return HttpResponse("<h1>Hello, world. You're at the Awesome Gym.</h1>")

#Selection and Projection Queries
def page1(request):
    #results = my_sql_query_8(request)
    #data = {'results': results}
    form = MyFormPage1(request.POST)
    data = {}
    Select = ""
    if request.method == "POST":
            if form.is_valid():
                EquipType = request.POST.get('EquipType', False)
                #if "EquipType2" in request.GET:
                if not request.POST.get("EquipType2", None) == None:
                #if request.POST.get("EquipType2", False) == "EquipType2":
                    Select += " EquipType"
                    print(Select)
                if not request.POST.get("EquipRate", None) == None:
                #if request.POST.get("EquipRate", False) == "EquipRate":
                    Select += " , EquipRate"
                    print(Select)
                #if request.POST["EquipDamageFee"]:
                if not request.POST.get("EquipDamageFee", None) == None:
                #if request.POST.get("EquipDamageFee", False) == "EquipDamageFee":
                    Select += " , EquipDamageFee"
                    print(Select)
            print("these are the things in select")

            print (Select)
            results = my_sql_query_1(request,Select,EquipType)
            data = {'results': results}
            return render(request, 'gym/page1.html', data)
    print(Select)
    return render(request, 'gym/page1.html', {'form':form})

#Join Queries
def page2(request):
    form = MyFormPage2(request.POST)
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            JoinQuery = request.POST["JoinQuery"]
            if JoinQuery == "Option 11":
                results2 = my_sql_query_6(request)
                data = {'results2': results2}
            return render(request, 'gym/page2.html', data)
    return render(request, 'gym/page2.html', {'form':form})


#Division Queries
def page3(request):
    form = MyFormPage3(request.POST)
    data = {}
    if request.method == "POST":
        if form.is_valid():
            DivisionQuery = request.POST["DivisionQuery"]
            if DivisionQuery == "Option 10":
                results = my_sql_query_7(request)
                data = {'results': results}
            return render(request, 'gym/page3.html', data)
    return render(request, 'gym/page3.html', {'form':form})

#Aggregation Query
def page4(request):
    form = MyFormPage4(request.POST)
    results3 = ""
    if request.method == "POST":
        if form.is_valid():
            AggregationQuery = request.POST["AggregationQuery"]
            if AggregationQuery == "Option 41":
                results3 = my_sql_query_8(request)  # OPTION 1
                print("Option1 was selected")
                print(results3)
            if AggregationQuery == "Option 42":
                results3 = my_sql_query_9(request)  # OPTION 2
                print("Option2 was selected")
                print(results3)
            data = {'results3': results3}
            return render(request, 'gym/page4.html', data)
    return render(request, 'gym/page4.html', {'form':form})

#Nested Aggregation by Group-By
def page5(request):
    form = MyFormPage5(request.POST)
    results4 = ""
    if request.method == "POST":
        if form.is_valid():
            NestedAggregationQuery = request.POST["NestedAggregationQuery"]
            if NestedAggregationQuery == "Option 31":
                results4 = my_sql_query_10(request)  # OPTION 1
                print("Option1 was selected")
                print(results4)
            if NestedAggregationQuery == "Option 32":
                results4 = my_sql_query_11(request)  # OPTION 2
                print("Option2 was selected")
                print
            data = {'results4': results4}
            return render(request, 'gym/page5.html', data)
    return render(request, 'gym/page5.html', {'form':form})

#testPage
def viewC(request):
    data = my_custom_sql(request)
    print(data)
    return render(request, 'gym/viewC.html', data)
# this is where we link the html to our app. where we put REST

#Delete Operation
@login_required
def page6(request):
    results = my_sql_query_13(request)           #OPTION 1 = DELETE WITH CASCADE
    results2 = my_sql_query_12(request)          #OPTION 2 = DELETE WITHOUT CASCADE
    data = {'results': results}
    return render(request, 'gym/page6.html', data)

#Update Operation
@login_required
def page7(request):
    results = my_sql_query_14(request)
    data = {'results': results}
    return render(request, 'gym/page7.html', data)


