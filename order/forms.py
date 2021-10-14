from django import forms
from .models import Order, GiftCart


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["payment_method"]


class Gift_CartForm(forms.ModelForm):
    class Meta:
        model = GiftCart
        fields = '__all__'
