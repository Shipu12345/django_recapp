from django import forms
from First_App.models import SignUP

class NewForm(forms.ModelForm):
    class Meta():
        model=SignUP
        fields='__all__'
