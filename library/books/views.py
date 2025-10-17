from django.shortcuts import render, redirect
from django.template.defaultfilters import title


# Create your views here.
def home(request):
    return render(request,template_name="home.html")
# def addbooks(request):
#     return render(request,template_name="addbook.html")


from books.forms import BookForm
from books.models import Book
def addbooks(request):
    if(request.method=="GET"):
        form_instance=BookForm()
        context={'books':form_instance}
        return  render(request,'addbook.html',context)
    if(request.method=="POST"):
        form_instance=BookForm(request.POST,request.FILES)
        if (form_instance.is_valid()):
            form_instance.save()
            # data=form_instance.cleaned_data
            # print(data)
            # t=data['title']
            # a=data['author']
            # p=data['price']
            # pa=data['pages']
            # l=data['language']
            # b=Book.objects.create(title=t,author=a,price=p,pages=pa,language=l)
            # b.save()
            return redirect('books:viewbooks')


def viewbooks(request):
    b=Book.objects.all()
    context = {'books': b}
    return render(request,"viewbook.html", context)
def bookdetail(request,i):
    if(request.method=="GET"):
        b = Book.objects.get(id=i)
        context = {"book": b}
        return render(request,'bookdetail.html',context)


def editbook(request,i):
    if (request.method == "GET"):
        b=Book.objects.get(id=i)
        form_instance=BookForm(instance=b)
        context={'form':form_instance}
        return render(request,'editbook.html',context)
    if (request.method == "POST"):
        b=Book.objects.get(id=i)
        form_instance = BookForm(request.POST, request.FILES,instance=b)
        if (form_instance.is_valid()):
            form_instance.save()
            return redirect('books:viewbooks')
def deletebook(request,i):
    if (request.method == "GET"):
        b=Book.objects.get(id=i)
        b.delete()
        return redirect('books:viewbooks')