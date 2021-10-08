from django import forms
from .models import Order, Gift_Cart


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["payment_method"]

class Gift_CartForm(forms.ModelForm):
    class Meta:
        model = Gift_Cart
        fields = '__all__'