from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Numbers,Emergency,Manchar

# Create your views here.
def home(request):
    return render(request,"Index.html", context=None)

def Emergency1(request):
    number1=Emergency.objects.all()
    num = {
        'no':number1
    }
    return render(request,"Emergency.html",context=num)

def ClgCampus(request):
    number=Numbers.objects.all()
    num = {
        'no':number
    }
    return render(request,"Numbers.html",context=num)

def MancharNos(request):
    number=Manchar.objects.all()
    num = {
        'no':number
    }
    return render(request,"Manchar.html",context=num)

def AboutUs(request):
    return render(request,"Aboutus.html", context=None)