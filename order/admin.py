from django.contrib import admin
from .models import Order, Gift_Cart, Cart, CartProduct


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass

@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Gift_Cart)
class GiftCartAdmin(admin.ModelAdmin):
    pass

