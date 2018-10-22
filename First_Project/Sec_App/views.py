from django.shortcuts import render
from Sec_App.forms import  UserForm,UserProfile_Form

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout




# Create your views here.


def home(request):
    return render(request,'Sec_App/base.html',context=None)

def registers(request):
    resistered=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfile_Form(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'picture' in request.FILES:
                profile.picture=request.FILES['picture']
            profile.save()

            resistered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfile_Form()

    return render(request,'First_App/signup.html',{
    'user_form':user_form,
    'profile_form':profile_form,
    'resistered':resistered
    })


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('AppTwo:home'))

@login_required
def special(request):
    return HttpResponse('You Are now logged In!')



def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('pass')


        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account Not Active')
        else:
            print('Login Failed...Someone Tried to login!')
            print('Username: {} and password {} '.format(username,password))
            return HttpResponse('Invalid Login Details.')
    else:
        return render(request,'Sec_App/login.html',context=None)
