from django.shortcuts import render

from .models import *
# Create your views here.


def home(request):
    products=Stocks.objects.all()
    return render(request,'home.html',{'products':products})

def product_details(request,pk):
    product=Stocks.objects.get(id=pk)
    return render(request,'product.detail',{'product':product})
    
