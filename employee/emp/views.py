from django.shortcuts import render, redirect
from emp.forms import employeeform
from emp.models import employee
# Create your views here.
def addemployee(request):
    if (request.method=="GET"):
        form_instance=employeeform
        context={'form':form_instance}
        return render(request,'addemp.html',context)
    if(request.method=="POST"):
        form_instance=employeeform(request.POST,request.FILES)
        if (form_instance.is_valid()):
          form_instance.save()
          # return render(request,'addemp.html')
          return redirect(viewemployees)
def viewemployees(request):
    if(request.method=="GET"):
        e=employee.objects.all()
        context={'employee':e}
        return render(request,'viewemp.html',context)