from urllib import request
from django.shortcuts import render
from .models import *
# Create your views here.



def home(request):
    stocks=Stocks.objects.all()
    # stocks=Stocks.objects.get(P_name='SSD')
    
    
    return render(request,'home.html',{'stocks':stocks})