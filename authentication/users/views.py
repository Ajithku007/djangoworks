from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout
from pyexpat.errors import messages
from users.forms import SignupForm
from users.forms import LoginForm
from django.contrib import messages


# Create your views here.
class home(View):
    def get(self,request):
        return render(request,'home.html')

class Register(View):
    def get(self,request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,'register.html',context)
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('userlogin')
        else:
            print(form_instance.errors)
            return render(request,'register.html',{'form':form_instance})


class userlogin(View):
    def get(self,request):
        form_instance=LoginForm()
        context={'loginform':form_instance}
        return render(request,'login.html',context)
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.cleaned_data['username']
            p=form_instance.cleaned_data['password']
            user=authenticate(username=u,password=p)
            #authenticate returns the user object if user with the given username and password exists in database
            #else return none
            if user:#if user exists
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"Invalid Credentials")
                return render(request,'login.html',{'loginform': form_instance})




class userlogout(View):
        def get(self,request):
            logout(request)
            return redirect('userlogin')