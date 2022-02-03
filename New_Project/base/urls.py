from django.urls import path

from . import views
# 

urlpatterns = [
    path('',views.home),
    path('product_detail/<str:pk>',views.product_details,name='product_detail'),
]
