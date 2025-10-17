from django.shortcuts import render, redirect
from django.template.defaultfilters import title
from django.templatetags.i18n import language
from django.db.models import Q

# Create your views here.
# def home(request):
#     return render(request,template_name="home.html")
from django.views import View
class Home(View):
    def get(self,request):
        return render(request,'home.html')


from books.forms import BookForm
from books.models import Book
class addbooks(View):
    def get(self,request):
        form_instance=BookForm()
        context={'books':form_instance}
        return  render(request,'addbook.html',context)
    def post(self,request):
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


class viewbooks(View):
    def get(self,request):
     b=Book.objects.all()
     context = {'books': b}
     return render(request,"viewbook.html", context)


class bookdetail(View):
    def get(self,request,i):
        b = Book.objects.get(id=i)
        context = {"book": b}
        return render(request,'bookdetail.html',context)


class editbook(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        form_instance=BookForm(instance=b)
        context={'form':form_instance}
        return render(request,'editbook.html',context)
    def post(self,request,i):
        b=Book.objects.get(id=i)
        form_instance = BookForm(request.POST, request.FILES,instance=b)
        if (form_instance.is_valid()):
            form_instance.save()
            return redirect('books:viewbooks')
class deletebook(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        b.delete()
        return redirect('books:viewbooks')

class search(View):
    def get(self,request):
        query=request.GET['q']
        if query:
            b=Book.objects.filter(Q(author__icontains=query)|Q(title=query)|Q(language=query))
            #Q object--useto add logical AND and logical OR in ORM queries
            #field lookups-->fieldname__lookup  eg:age__gt=30 , age__lt=30,title__icontains="abcd"
            context={'book':b}
        return render(request,'search.html',context)