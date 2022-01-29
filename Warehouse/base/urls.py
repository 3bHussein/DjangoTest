from django import views
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home),
    path('stock/<str:pk>',views.stockD,name='stock')
    
]
