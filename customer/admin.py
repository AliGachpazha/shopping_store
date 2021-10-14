from django.contrib import admin
from .models import  User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email','phone', 'username']
    search_fields = ['email', 'username']
