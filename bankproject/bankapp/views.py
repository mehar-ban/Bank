from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect

from . models import Team


# Create your views here.
def demo(request):
    obj=Team.objects.all()
    return render(request,"index.html",{'result':obj})

def register(request):
    if request.method == 'POST.get':
        username = request.POST.get['username']
        password = request.POST.get['password']
        cpassword = request.POST.get['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                messages.info(request,"user created")
                return render(request,"login.html")

        else:
            print("Password not Matching")
            return redirect('register')
    return render(request,"register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)

            return redirect('/')
            # return render(request,"form.html")

        else:
            messages.info(request,"invalid user")
            # return redirect('')
    return render(request,"login.html")
def form(request):
    return render(request,"form.html")

def newpage(request):
    return render(request,"newpage.html")

def msg(request):
    return render(request,"index.html")
def logout(request):
    # auth.logout(request)
    # return redirect('/')
    return render(request,"index.html")
