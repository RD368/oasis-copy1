from django.contrib import admin
from django.urls import path,include
from  . import views

urlpatterns = [
    path('/login',views.login_view,name= 'Login'),
    path('/signup',views.register,name= 'Signup'),
    path('/logout',views.logout_view,name= 'Logout'),
]
