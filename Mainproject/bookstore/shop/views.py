from django.shortcuts import render,redirect
from shop.models import Category,Book
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
def allcategories(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})

def allbooks(request,p):
    c=Category.objects.get(name=p)
    p=Book.objects.filter(category=c)
    return render(request, 'book.html',{'c':c,'p':p})

def detail(request,p):
    book=Book.objects.get(name=p)

    return render(request,'detail.html',{'p':book})

def register(request):
    if request.method == "POST":
        u = request.POST['u']
        p = request.POST['p']
        cp =request.POST['cp']
        e  =request.POST['e']


        if(p==cp):
            u=User.objects.create_user(username=u,password=p,email=e)
            u.save()
            return redirect('shop:allbook')
        else:
            return HttpResponse("Password Not Matching")

    return render(request,'register.html')
def user_login(request):
    if request.method=="POST":
        name=request.POST['u']
        pass1=request.POST['p']
        user=authenticate(username=name,password=pass1)
        if user:
            login(request,user)
            return redirect('shop:allbook')
        else:
            messages.error(request,"Invalid Credentials")
    return render(request,'login.html')


@login_required
def user_logout(request):
    logout(request)
    return user_login(request)