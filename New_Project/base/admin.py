from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Stocks)
class StocksAdmin(admin.ModelAdmin):
    list_display=['name','count','status','suppler_id']
    
admin.site.register(Supplers)

    
# admin.site.register(Stocks)