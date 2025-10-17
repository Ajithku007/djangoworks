from django.contrib.auth.forms import UserCreationForm
from django import forms
from user.models import CustomUser


class SignupForm(UserCreationForm):
    role_choice=(('teacher','Teacher'),('student','Student'))
    role=forms.ChoiceField(choices=role_choice)
    gender_choice=(('male','Male'),('female','Female'))
    gender=forms.ChoiceField(choices=gender_choice,widget=forms.RadioSelect)
    class Meta:
        model=CustomUser
        fields=["username","password1","password2","email","first_name","last_name","phone","gender","role"]


class LoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput)