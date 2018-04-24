from django.contrib import admin
from .models import Product,Menu,Item
# Register your models here.

admin.register(Product,Menu,Item)(admin.ModelAdmin)