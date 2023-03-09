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

def Change_Info(request,pk):
    user=User.objects.get(id=pk)
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        first_name=request.POST["firstname"]
        last_name=request.POST["lastname"]
        if user.email!=email:
            if User.objects.filter(email=email).exists():
                return render(request,f"user/change.html",{"msg":"kullanıcı mevcut lütfen baska email girniz",
                "email":email,
                "first_name":first_name,
                "last_name":last_name,})
            user.email=email
            user.save()
        if user.username!=username:
            if User.objects.filter(username=username).exists():
                return render(request,f"user/change.html",{"msg":"kullanıcı mevcut lütfen baska username girniz",
                "email":email,
                "first_name":first_name,
                "last_name":last_name,})
            user.username=str(username)
            user.save()
        if user.first_name!=first_name:
            user.first_name=first_name
            user.save()
        if user.last_name!=last_name:
            user.last_name=last_name
            user.save()                       
        return redirect("index")
         
    return render(request,"user/change.html",{ "email":user.email,
                    "username":user.username,
                    "firstname":user.first_name,
                    "lastname":user.last_name,})


def Change_Password(request,pk):# 2. form buraya gelmiyor 
    user=User.objects.get(id=pk)
    if request.method=="POST":
        current_pas=request.POST["current_password"]
        new_password=request.POST["new_password"]
        again_password=request.POST["again_password"]
        if user.check_password(current_pas):
            if new_password==again_password:
                user.set_password(new_password)
                user.save()
                login(request,user)
                return redirect("index")
            else:
                return render(request,"user/change.html",{"msg":"passwords are not same"})
        else:
            return render(request,"user/change.html",{"msg":"old password is not true"})
    return render(request,"user/change.html")

def delete_user(request,pk):
    user=User.objects.get(id=pk)
    user.delete()
    return redirect("index")


   
   

