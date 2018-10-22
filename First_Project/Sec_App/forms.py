from django import forms
from django.contrib.auth.models import User
from Sec_App.models import UserProfile



class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')



class UserProfile_Form(forms.ModelForm):

    class Meta():
        model=UserProfile
        fields=('portfolio','picture')

    
