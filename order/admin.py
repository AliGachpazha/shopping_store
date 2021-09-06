from django.contrib import admin
from .models import Order, OrderItem, Gift_Cart


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Gift_Cart)
class GiftCartAdmin(admin.ModelAdmin):
    pass

