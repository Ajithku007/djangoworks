from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,template_name="register.html")
def login(request):
    return render(request,template_name="login.html")
def logout(request):
    return render(request,template_name="logout.html")