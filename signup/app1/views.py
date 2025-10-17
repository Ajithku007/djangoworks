from django.shortcuts import render
from app1.forms import signupForm


# Create your views here.
def signup(request):

    if (request.method=="POST"):
        form_instance=signupForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            username=data['username']
            password=data['password']
            place=data['place']
            gender=data['gender']
            role=data['role']
            email=data['email']
            details={'username':username,'password':password,'place':place,'gender':gender,'role':role,'email':email}
            context={'details':details}
            return render(request,'signup.html',context)








    if (request.method=="GET"):
        form_instance=signupForm()
        context={'result':form_instance}
        return render(request,'signup.html',context)