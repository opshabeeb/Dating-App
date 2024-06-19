from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('about', views.AboutView.as_view(), name='about'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('login', views.LoginView.as_view(), name='login'),
    path('matching', views.MatchingView.as_view(), name='matching'),
    path('test', views.TestView.as_view(), name='test'),
    path('createprofile', views.CreateProfileView.as_view(), name='createprofile'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('plans', views.PlansView.as_view(), name='plans'),
]
