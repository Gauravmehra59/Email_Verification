from django.contrib import admin
from django.urls import path
from . import views
from .views import Signupview , login
from app import views
urlpatterns = [
    path('',views.home,name="home"),
    path('login/',login.as_view(),name="login"),
    path('signup/',Signupview.as_view(),name="signup"),
    path('account-verify/<slug:token>',views.account_verify,name="account_verify")
    
]
