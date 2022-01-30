from datetime import datetime
from operator import mod
from this import d
from tkinter.tix import Tree
from django.db import models

# Create your models here.




class Stocks(models.Model):
    status_CHOICES=[('A','Available'),('O','Out')]
    # P_id=models.IntegerField(primary_key=True)
    P_id=models.AutoField(primary_key=True)
    P_name=models.CharField(max_length=100)
    P_count=models.IntegerField()
    P_status=models.CharField(max_length=1,choices=status_CHOICES)
    P_Date=models.DateTimeField(default=datetime.now,blank=True)
    S_id=models.ForeignKey('Suppler',on_delete=models.CASCADE)
    P_description=models.TextField(blank=True,null=True)



    def __str__(self):
        return self.P_name
    
class Suppler(models.Model):
    S_id=models.IntegerField(primary_key=True)
    S_name=models.CharField(max_length=100)
    S_descrition=models.TextField(blank=True,null=True)
    S_email=models.EmailField(blank=True)
    
    # def __init__(self):
    #     self.S_name
    def __str__(self):
        return self.S_name
 
    
    
    


        

    