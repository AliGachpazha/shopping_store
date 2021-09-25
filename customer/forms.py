from django import forms

from .models import User
from .vars import USER_TYPE_CHOICES, USER_TYPE, USERNAME, PASSWORD


class UserForms(forms.ModelForm):
    # confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'phone', 'email', 'first_name', 'last_name', 'password',  ]


class UserLogin(forms.Form):
    username = forms.CharField(max_length=1000, label=USERNAME)
    password = forms.CharField(max_length=1000, widget=forms.PasswordInput(), label=PASSWORD)
    user_type = forms.ChoiceField(
        widget=forms.Select,
        choices=USER_TYPE_CHOICES,
        label=USER_TYPE
    )

class EditProfile(forms.ModelForm):
    NewPassword = 'NewPassword '
    NewPasswordConfirm = 'NewPasswordConfirm'
    new_password =forms.CharField(max_length=1000, widget=forms.PasswordInput(), label=NewPassword)
    new_passwordconfirm = forms.CharField(max_length=1000, widget=forms.PasswordInput(), label=NewPasswordConfirm)
    class Meta:
        model = User
        fields = ['email', 'phone','first_name', 'last_name','new_password','new_passwordconfirm']