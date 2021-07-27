
from django import forms
from django.forms import fields
from . models import Signup

class SignupForm(forms.ModelForm):
    class Meta():
        model=Signup
        fields='__all__'
        
class LoginForm(forms.ModelForm):
    Password=forms.CharField(max_length=10,widget=forms.PasswordInput)
    class Meta():
        model=Signup
        fields=('Email','Password')
        
class UpdateForm(forms.ModelForm):
    class Meta():
        model=Signup
        fields=('Name','Email','Age','Photo')
        
class ChangePasswordForm(forms.Form):
    OldPassword=forms.CharField(max_length=10,widget=forms.PasswordInput)
    NewPassword=forms.CharField(max_length=10,widget=forms.PasswordInput)    
    ConfirmNewPassword=forms.CharField(max_length=10,widget=forms.PasswordInput)
    



        
    