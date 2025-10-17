from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2","email"]
        # help_texts={
        #     'username':' ',
        #     'password':' ',
        #     'password2':' '
        #
        # }
    def __init__(self,*args,**kwargs):
            super(SignupForm,self).__init__(*args,**kwargs)
            self.fields['username'].help_text=None
            self.fields['password1'].help_text=None
            self.fields['password2'].help_text=None


class Loginform(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput)