
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from user.forms import SignupForm
from user.forms import LoginForm
from django.core.mail import send_mail

from user.models import CustomUser


# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')

class AdminHome(View):
    def get(self,request):
        return render(request,'adminhome.html')


class StudentHome(View):
    def get(self,request):
        return render(request,'studenthome.html')


class TeacherHome(View):
    def get(self,request):
        return render(request,'teacherhome.html')


class Register(View):
    def get(self,request):
        form_instance = SignupForm()
        context={'form':form_instance}
        return render(request,'register.html',context)
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.save(commit=False)
            u.is_active=False
            u.save()
            u.generate_otp()
            send_mail(
                "Django Auth OTP",
                 u.otp,
                "ajithcr070@gmail.com",
                [u.email],
                fail_silently=False,
            )
            return redirect('otp')
        else:
            print("error")
            return render(request, 'register.html', {'form':form_instance})


class otpverification(View):
    def get(self,request):
        return render(request,'otp.html')
    def post(self,request):
        o=request.POST['o']
        try:
            u=CustomUser.objects.get(otp=o)
            u.is_verified=True
            u.is_active=True
            u.otp=None
            u.save()
            return redirect('login')
        except:
            messages.error(request,"Invalid Otp")
            return redirect('otp')




class Userlogin(View):
    def get(self,request):
        form_instance=LoginForm()
        context={'form':form_instance}
        return render(request,'login.html',context)
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.cleaned_data['username']
            p=form_instance.cleaned_data['password']
            user=authenticate(username=u,password=p)
            #authenticate returns the user object if user with the given username and password exists in database
            #else return none
            if user and user.is_superuser:#if user exists
                login(request,user)
                return redirect('adminhome')
            elif user and user.role=="teacher":#if user exists
                login(request,user)
                return redirect('teacherhome')
            elif user and user.role=="student":#if user exists
                login(request,user)
                return redirect('studenthome')
            else:
                messages.error(request,"Invalid Credentials")
                return render(request,'login.html',{'loginform': form_instance})


class Userlogout(View):
    def get(self,request):
        logout(request)
        return redirect('login')

