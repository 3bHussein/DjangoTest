from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Stocks)

@admin.register(Stocks)
class stock(admin.ModelAdmin):
    list_display=['name','count','statue','suppler_id']



admin.site.register(Supplers)


