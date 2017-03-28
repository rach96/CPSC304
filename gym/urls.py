from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^viewC/$', views.viewC, name='viewC'),
    url(r'^page1/$', views.page1, name='Page1'),
    url(r'^page2/$', views.page2, name='Page2'),
    url(r'^page3/$', views.page3, name='Page3'),
    url(r'^page4/$', views.page4, name='Page4'),
    url(r'^page5/$', views.page5, name='Page5'),
    url(r'^page6/$', views.page6, name='Page6'),
    url(r'^page7/$', views.page7, name='Page7')
]
