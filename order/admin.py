from django.contrib import admin
from .models import Order, GiftCart, Cart, CartProduct


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'created_at']
    search_fields = ['customer', ]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass

@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    pass


@admin.register(GiftCart)
class GiftCartAdmin(admin.ModelAdmin):
    list_display = ['user','code','date']
    search_fields = ['user' ]
