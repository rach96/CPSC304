# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpRequest
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext
from django.db import IntegrityError

from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import login as view_login
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views.generic.edit import CreateView
import json
from .forms import MyFormPage1
from .forms import MyFormPage2
from .forms import MyFormPage3
from .forms import MyFormPage4
from .forms import MyFormPage5
from .forms import UserLoginForm
from .forms import MyFormPage6
from .forms import MyFormPage7
from .forms import MyFormPage8

from gym.query import my_custom_sql,my_sql_query_1,my_sql_query_2,my_sql_query_7,my_sql_query_5,my_sql_query_8,\
    my_sql_query_9,my_sql_query_10,my_sql_query_11,my_sql_query_12,my_sql_query_13,my_sql_query_14,my_sql_query_7_insert

def homepage(request):
    #my_custom_sql(request)
    data = {}
    return render(request, 'gym/homepage.html',data)

#Selection and Projection Queries
def page1(request):
    form = MyFormPage1(request.POST)
    Select = ""
    if request.method == "POST":
            if form.is_valid():
                EquipType = request.POST.get('EquipType', False)
                if not request.POST.get("EquipType2", None) == None:
                    Select += " EquipType"
                    print(Select)
                if not request.POST.get("EquipRate", None) == None:
                    if Select == "":
                        Select += " EquipRate"
                    else:
                        Select += " , EquipRate"
                    print(Select)
                if not request.POST.get("EquipDamageFee", None) == None:
                    if Select == "":
                        Select += " EquipDamageFee"
                    else:
                        Select += " , EquipDamageFee"
                    print(Select)
            print("these are the things in select")

            print (Select)
            results = my_sql_query_1(request,Select,EquipType)
            data = {'results': results}
            return render(request, 'gym/page10.html', data)
    else:
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
                results = my_sql_query_5(request)
                data = {'results': results}
            return render(request, 'gym/page10.html', data)
    print({'form': form})
    return render(request, 'gym/page2.html', {'form':form})


#Division Queries
def page3(request):
    form = MyFormPage3(request.POST)
    if request.method == "POST":
        if form.is_valid():
            DivisionQuery = request.POST["DivisionQuery"]
            if DivisionQuery == "Option 10":
                results = my_sql_query_7(request)
            if DivisionQuery == "Option 12":
                results = my_sql_query_7_insert(request)

            data = {'results': results}
            return render(request, 'gym/page10.html', data)
    print({'form':form})
    return render(request, 'gym/page3.html', {'form': form})

#Aggregation Query
def page4(request):
    form = MyFormPage4(request.POST)
    if request.method == "POST":
        if form.is_valid():
            AggregationQuery = request.POST["AggregationQuery"]
            if AggregationQuery == "Option 41":
                results = my_sql_query_8(request)  # OPTION 1
            if AggregationQuery == "Option 42":
                results = my_sql_query_9(request)  # OPTION 2
            data = {'results': results}
            return render(request, 'gym/page10.html', data)
    return render(request, 'gym/page4.html', {'form':form})

#Nested Aggregation by Group-By
def page5(request):
    form = MyFormPage5(request.POST)
    results = ""
    if request.method == "POST":
        if form.is_valid():
            NestedAggregationQuery = request.POST["NestedAggregationQuery"]
            if NestedAggregationQuery == "Option 31":
                results = my_sql_query_10(request)  # OPTION 1
            if NestedAggregationQuery == "Option 32":
                results = my_sql_query_11(request)  # OPTION 2
            data = {'results': results}
            return render(request, 'gym/page10.html', data)
    return render(request, 'gym/page5.html', {'form':form})

#testPage
def viewC(request):
    data = my_custom_sql(request)
    print(data)
    return render(request, 'gym/viewC.html', data)
# this is where we link the html to our app. where we put REST


#Delete WITHOUT CASCADE Operation
@login_required
def page6(request):
    form = MyFormPage6(request.POST)
    if request.method == "POST":
        if form.is_valid():
            DeleteQuery = request.POST["DeleteQuery"]
            if DeleteQuery == "Option 6":
                CustomerToDelete = request.POST.get('CustomerToDelete', False)
                results = my_sql_query_12(request,CustomerToDelete)
                print(results)
            data = {'results': results}
            return render(request, 'gym/page10.html', data)
    return render(request, 'gym/page6.html', {'form':form})

#Delete ON CASCADE Operation
@login_required
def page8(request):
    form = MyFormPage8(request.POST)
    if request.method == "POST":
        if form.is_valid():
            DeleteQuery = request.POST["DeleteOnCascadeQuery"]
            if DeleteQuery == "Option 12":
                CustomerToDelete2 = request.POST.get('CustomerToDelete2', False)
                try:
                    results = my_sql_query_13(request, CustomerToDelete2)
                    print(results)
                except IntegrityError as e:
                    return render_to_response('gym/page9.html', {"message":e.__cause__})
            data = {'results': results}
            return render(request, 'gym/page10.html', data)
    return render(request, 'gym/page8.html', {'form':form})

#Update Operation
@login_required
def page7(request):
    form = MyFormPage7(request.POST)
    if request.method == "POST":
        if form.is_valid():
            UpdateQuery = request.POST["UpdateQuery"]
            if UpdateQuery == "Option 7":
                ToUpdateChar = request.POST.get('ToUpdateChar', False)
                message = "An error has occured"
                try:
                    results = my_sql_query_14(request,ToUpdateChar)
                except IntegrityError as e:
                    return render_to_response('gym/page9.html', {"message":e.__cause__})
            data = {'results': results}
            return render(request, 'gym/page10.html', data)
    return render(request, 'gym/page7.html', {'form':form})



# Use Django's built in login system but redirect to the homepage if already
# logged in
def user_login(request, **kwargs):
    form = UserLoginForm(request.POST)
    next = request.GET.get('next', '/homepage/')
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        #username = request.POST['username']
        #password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                view_login(request,user)
                return redirect(request.GET.get('next',settings.LOGIN_REDIRECT_URL))

        else:
            return HttpResponseRedirect(settings.LOGIN_URL)


def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)