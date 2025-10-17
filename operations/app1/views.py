from django.shortcuts import render


# Create your views here.


def addition(request):
    if (request.method=="POST"):
        print(request.POST)
        n1=int(request.POST['n1'])
        n2=int(request.POST['n2'])
        s=n1+n2
        context={'result':s}
        return render(request, 'addition.html',context)
    if (request.method=="GET"):
        return render(request,'addition.html')

def factorial(request):
    if (request.method=="POST"):

        n=int(request.POST['n'])
        f=1
        for i in range(1,n+1):
            f*=i
        context={'result':f}
        return render(request, 'factorial.html',context)
    if (request.method=="GET"):
        return render(request,'factorial.html')

def bmi(request):
    if (request.method=="POST"):

        w=float(request.POST['w'])
        h=float(request.POST['h'])/100
        b=w/(h**2)
        context={'result':b}
        return render(request, 'bmi.html',context)
    if (request.method=="GET"):
        return render(request,'bmi.html')
