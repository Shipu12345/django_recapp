from django.contrib import admin
from django.urls import path,include
from Sec_App import views


app_name='AppTwo'

urlpatterns = [
    path('home',views.home,name='home'),
    path('sign',views.registers,name='sign_up'),
    path('signin',views.user_login,name='sign_in'),
    path('logout',views.user_logout,name='sign_out'),
    path('special',views.special,name='special'),
]
