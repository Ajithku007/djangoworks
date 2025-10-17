from django.shortcuts import render

# Create your views here.
def third(request):
    return render(request,template_name="third.html")

def fourth(request):
    return render(request,template_name="fourth.html")