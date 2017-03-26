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

def page1(request):
    #return HttpResponse("This is where the aggregations will go")
    results = my_sql_query_8(request)
    data = {'results' : results}
    # render_to_response('page1.html',{'results' : results}, context_instance=RequestContext(request))
    return render(request, 'gym/page1.html', data)

def page2(request):
    data = {'request': request}
    #return HttpResponse("This is where the projections will go")
    return render(request, 'gym/page2.html', data)

#testPage
def viewC(request):
    data = my_custom_sql(request)
    print(data)
    return render(request, 'gym/viewC.html', data)
# this is where we link the html to our app. where we put REST

@login_required
def page3(request):
    data = {}
    #return HttpResponse("This is where we can delete tuples in clean room")
    return render(request, 'gym/page3.html', data)

@login_required
def page4(request):
    data = {}
    #return HttpResponse("This is where we can update items OR delete items so that there is a cascade")
    return render(request, 'gym/page4.html', data)


