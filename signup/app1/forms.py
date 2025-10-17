from django import  forms

class signupForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
    place=forms.CharField()
    gender=forms.CharField()
    role=forms.CharField()
    email=forms.EmailField()