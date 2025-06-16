from django.contrib import admin
from .models import Product, Category
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price',)
    fields = ('name', 'category', 'description', 'price', 'image',)
admin.site.register(Category)