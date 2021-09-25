from django import forms
from .models import Order, Gift_Cart


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["ordered_by", "shipping_address",
                  "mobile", "email", "payment_method","customer"]

class Gift_CartForm(forms.ModelForm):
    class Meta:
        model = Gift_Cart
        fields = '__all__'