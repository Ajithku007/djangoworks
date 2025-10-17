from django.shortcuts import render, redirect

from app1.forms import Moveiform
from app1.models import Moviedetail




# Create your views here.
def movielist(request):
    b = Moviedetail.objects.all()
    context = {'view': b}
    return  render(request,"movielist.html",context)
def addmovies(request):
    if (request.method=="GET"):
      form_instance=Moveiform()
      context={'form':form_instance}
      return render(request,"addmovies.html",context)
    if(request.method=="POST"):
        form_instance=Moveiform(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('movielist')

def movieDetails(request,i):
    b=Moviedetail.objects.get(id=i)
    context={'detail':b}
    return render(request,'detail.html',context)

def update(request,i):
    if(request.method=="GET"):
        b=Moviedetail.objects.get(id=i)
        form_instance=Moveiform(instance=b)
        context = {'form': form_instance}
        return render(request,'update.html',context)
    if(request.method=="POST"):
        b=Moviedetail.objects.get(id=i)
        form_instance = Moveiform(request.POST, request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('movielist')

def deletemovie(request,i):
    if(request.method=="GET"):
        b=Moviedetail.objects.get(id=i)
        b.delete()
        return redirect('movielist')