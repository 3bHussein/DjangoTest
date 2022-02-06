from tkinter import CASCADE
from django.db import models


# Create your models here.

class Stocks(models.Model):
    statue_choice=[('A','Available'),('O','outStock')]
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    statue=models.CharField(max_length=10,choices=statue_choice)
    count=models.IntegerField()
    suppler_id=models.ForeignKey('Supplers',on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Supplers(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

