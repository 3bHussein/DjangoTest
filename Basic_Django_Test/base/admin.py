from django.contrib import admin
from .models import *


# admin.site.register(Stocks)
@admin.register(Stocks)
class StocksAdmin(admin.ModelAdmin):
    list_display=['P_name','P_count','P_status']
    
admin.site.register(Suppler)