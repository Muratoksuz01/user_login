from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.models import User


# Create your views here.

def Index(request):
    return render(request,"user/Index.html")

def Register(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method=="POST":
        username=request.POST["username"]
        name=request.POST["firstname"]
        lastname=request.POST["lastname"]
        email=request.POST["email"]
        password=request.POST["password"]
        rpassword=request.POST["repassword"]
        if rpassword==password:
            if User.objects.filter(username=username).exists():
                return render(request,"user/register.html",{"msg":"kullanıcı mevcut lütfen baska usernamae girniz",
                    "email":email,
                    "firstname":name,
                    "lastname":lastname,})
            if User.objects.filter(email=email).exists():
                return render(request,"user/register.html",{"msg":"kullanıcı mevcut lütfen baska email girniz",
                    "username":username,
                    "firstname":name,
                    "lastname":lastname,})

            user=User.objects.create_user(username=username,first_name=name,last_name=lastname,email=email,password=password)
            user.save()
            return redirect("index")
        else:
            return render(request,"user/register.html",{"msg":"passwords are not same", 
                    "email":email,
                    "username":username,
                    "firstname":name,
                    "lastname":lastname,
                    })

    return render(request,"user/register.html")

def Login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("index")
        

    return render(request,"user/login.html")
def Logout(request):
    logout(request)
    return redirect("index")

def Change(request,id):
    user=User.objects.get(id=id)
    




