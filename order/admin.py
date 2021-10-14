from django.contrib import admin
from .models import Order, GiftCart, Cart, CartProduct


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


@admin.register(GiftCart)
class GiftCartAdmin(admin.ModelAdmin):
    pass
