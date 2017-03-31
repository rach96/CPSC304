from django.conf.urls import url
from django.contrib import admin
from gym.views import (user_login)
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^viewC/$', views.viewC, name='viewC'),
    url(r'^page1/$', views.page1, name='Page1'),
    url(r'^page2/$', views.page2, name='Page2'),
    url(r'^page3/$', views.page3, name='Page3'),
    url(r'^page4/$', views.page4, name='Page4'),
    url(r'^page5/$', views.page5, name='Page5'),
    url(r'^page6/$', views.page6, name='Page6'),
    url(r'^page8/$', views.page8, name='Page8'),
    url(r'^page7/$', views.page7, name='Page7'),
    url(r'^admin/', admin.site.urls),
]
