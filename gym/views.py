# Create your views here.
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.template import RequestContext


from gym.query import my_custom_sql,my_sql_query_1,my_sql_query_2,my_sql_query_7,my_sql_query_6,my_sql_query_5,my_sql_query_8,\
    my_sql_query_9,my_sql_query_10,my_sql_query_11,my_sql_query_12,my_sql_query_13,my_sql_query_14

def index(request):
    return HttpResponse("Hello, world. You're at the Awesome Gym.")

#Selection and Projection Queries
def page1(request):
    results = my_sql_query_8(request)
    data = {'results': results}
    return render(request, 'gym/page1.html', data)

#Join Queries
def page2(request):
    results1 = my_sql_query_5(request)          #OPTION 1
    results2 = my_sql_query_6(request)          #OPTION 2
    data = {'results2': results2}
    return render(request, 'gym/page2.html', data)

#Division Queries
def page3(request):
    results = my_sql_query_7(request)
    data = {'results': results}
    return render(request, 'gym/page3.html', data)

#Aggregation Query
def page4(request):
    results = my_sql_query_8(request)           #OPTION 1
    results2 = my_sql_query_9(request)          #OPTION 2
    data = {'results' : results}
    return render(request, 'gym/page4.html', data)

#Nested Aggregation by Group-By
def page5(request):
    results = my_sql_query_10(request)          #OPTION 1
    results2 = my_sql_query_11(request)         #OPTION 2
    data = {'results': results}
    return render(request, 'gym/page5.html', data)

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


