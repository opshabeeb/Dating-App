from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('matching',views.matching,name='matching'),
    path('test',views.test,name='test'),
    path('createprofile',views.create_profile,name='createprofile'),
    path('profile',views.profile_view,name='profile'),
    path('plans',views.plans,name='plans'),
]