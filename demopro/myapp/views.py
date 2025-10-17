from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def Page1(request):
#     return HttpResponse("First Page")
# def Page2(request):
#     return HttpResponse("Second Page")

def first(request):
    context={"name":"arun","age":22} #context is a dictionary type
                                       #is used to pass data from views to html pages
    return render(request,'firstpage.html',context)
def second(request):
    context={"place":"palakkad","salary":12345}
    return render(request,'secondpage.html',context)