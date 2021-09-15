from django.contrib import admin
from .models import Address, User


# Register your models here.


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
