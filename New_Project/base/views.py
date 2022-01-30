from django.shortcuts import render

from .models import *
# Create your views here.


def home(request):
    products=Stocks.objects.all()
    return render(request,'home.html',{'products':products})