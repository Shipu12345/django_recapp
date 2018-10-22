from django.contrib import admin
from django.urls import path
from First_App import views

app_name='First_A'

urlpatterns = [

    path('new',views.index1,name='index'),
    path('list',views.customer_list,name='fal'),
    path('forms',views.form_name_view,name='form_test'),
    # path('sign',views.form_of_newForm,name='sign_up'),
    
]
