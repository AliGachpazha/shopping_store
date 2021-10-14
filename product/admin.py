from django.contrib import admin
from .models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    search_fields = ['name',]


@admin.register(Product)
class Productdmin(admin.ModelAdmin):
    list_display = ['title','category','created_at','updated_at']
    search_fields = ['title']
