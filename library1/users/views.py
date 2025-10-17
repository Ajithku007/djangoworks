from django.shortcuts import render, redirect
from django.views import View
from users.forms import SignupForm
from django.contrib.auth import authenticate,login,logout
from users.forms import Loginform
from django.contrib import messages


# Create your views here.
class register(View):
    def get(self,request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,"register.html",context)
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('users:login')
        else:
            print(form_instance.errors)
            return render(request,'register.html')



class userlogin(View):
    def get(self,request):
        form_instance=Loginform()
        context={'form':form_instance}
        return render(request,"login.html",context)
    def post(self,request):
        form_instance=Loginform(request.POST)
        if form_instance.is_valid():
            u=form_instance.cleaned_data["username"]
            p=form_instance.cleaned_data["password"]
            user=authenticate(username=u,password=p)
            if user:
                login(request,user)
                return redirect('books:home')
            else:
                messages.error(request,"Invalid credentials")
                return render(request,'login.html',{'form':form_instance})



class userlogout(View):
    def get(self,request):
        logout(request)
        return redirect("users:login")