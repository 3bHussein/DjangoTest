from urllib import request
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.



def home(request):
    stocks=Stocks.objects.all()
    # stocks=Stocks.objects.get(P_name='SSD')
    return render(request,'home.html',{'stocks':stocks})


def stockD(request,pk):
    try:
        stock=Stocks.objects.get(P_id=pk)
    except:
        return HttpResponse(f'<h1 style="text-align:center">Stock in not availabl</h1>')

        
   
   
    return render(request,'stockd.html',{'stock':stock}) 
 
        
        
        