from django.contrib import admin
from .models import Customer, Address, Management


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    pass
