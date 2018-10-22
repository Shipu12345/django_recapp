from django import forms
from django.core import validators

def ckeck_for_z(value):
    if value[0].lower()!='s':
        raise forms.ValidationError("Name Must start with 's' ")

class Form_Name(forms.Form):
    name=forms.CharField(validators=[ckeck_for_z])
    date=forms.DateField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label='Enter again your email')
    text=forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean=super().clean()
        Email=all_clean['email']
        Verify_email=all_clean['verify_email']
        if Email != Verify_email:
            raise forms.ValidationError("Make sure both emails are same.")







    # botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])


    # def clean_botcatcher(self):
    #     b=self.cleaned_data['botcatcher']
    #     if len(b)>0:
    #         raise forms.ValidationError('Gotcha Bot!')
    #     return b
