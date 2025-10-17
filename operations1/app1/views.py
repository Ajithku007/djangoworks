from django.shortcuts import render

from app1.forms import AdditionForm

# Create your views here.
def addition(request):
    if (request.method=="POST"):
        print(request.POST)
        #creating form instance using submitted data
        form_instance=AdditionForm(request.POST)
        #check weather the data is valid
        if form_instance.is_valid():
            #process data
            data=form_instance.cleaned_data
            n1=data['num1']
            n2=data['num2']
            s=int(n1)+int(n2)
            context={'result':s,'form':form_instance}


        return render(request, 'addition.html',context)

    if (request.method == "GET"):
         form_instance = AdditionForm()
         context = {'form': form_instance}
         return render(request, 'addition.html', context)

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



from app1.forms import BMIform
def bmi(request):
    if(request.method=="POST"):
        # create an form instance using submitted data
        form_instance=BMIform(request.POST)

        if form_instance.is_valid():
            data=form_instance.cleaned_data
            w=data['weight']
            h=data['height']/100
            # result=int(w)/(int(h)**2)
            result = float(w) / (float(h) ** 2)
            context={'bmivalue':result,'bmi':form_instance}
            return render(request,'bmi.html',context)


    if (request.method=="GET"):
       form_instance=BMIform()
       context={'bmi':form_instance}
       return  render(request,'bmi.html',context)


from app1.forms import signupForm
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
            print(details)
            context={'details':details}
            return render(request,'signup.html',context)

    if (request.method == "GET"):
        form_instance = signupForm()
        context = {'result': form_instance}
        return render(request, 'signup.html', context)


from app1.forms import calorieform
def calories(request):
    if(request.method=="GET"):
        form_instance=calorieform()
        context={'calories':form_instance}
        return  render(request,'caloriecalculator.html',context)

    if (request.method == "POST"):

        form_instance = calorieform(request.POST)

        if form_instance.is_valid():
            data = form_instance.cleaned_data
            w = data['weight']
            h = data['height']
            g=data['gender']
            a=data['age']
            al=data['activity_level']
            if g=="male":
                bmr=10 * w + 6.25 * h - 5 * a+ 5

            else:
                bmr=10 * w + 6.25 * h - 5 * a - 161
            c=int(bmr*float(al))
            context={'calorie_value':c,'calories':form_instance}
            return render(request, 'caloriecalculator.html', context)