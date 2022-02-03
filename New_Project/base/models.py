from tkinter import CASCADE
from turtle import update
from django.db import models

# Create your models here.

class Stocks(models.Model):
    status_choice=[('A','Aviable'),('O','OutStock')]
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    status=models.CharField(max_length=1,choices=status_choice)
    count=models.IntegerField()
    # image=models.ImageField(upload_to='base/static/img/products')
    image=models.ImageField(upload_to='img/products')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    suppler_id=models.ForeignKey('Supplers',on_delete=models.CASCADE)   
        
    def __str__(self):
        return self.name
        
    
class Supplers(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
