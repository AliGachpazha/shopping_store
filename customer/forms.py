from django import forms

from .models import User
from .vars import USER_TYPE_CHOICES, USER_TYPE, USERNAME, PASSWORD


class UserForms(forms.ModelForm):
    # confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'phone', 'email', 'first_name', 'last_name', 'password']


class UserLogin(forms.Form):
    username = forms.CharField(max_length=1000, label=USERNAME)
    password = forms.CharField(max_length=1000, widget=forms.PasswordInput(), label=PASSWORD)


class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'phone', 'first_name', 'last_name','address','city','post_code']


class ChangePasswordForm(forms.ModelForm):
    #password = forms.CharField(max_length=150, required=True, widget=forms.PasswordInput())
    new_password = forms.CharField(max_length=150, required=True, widget=forms.PasswordInput())
    new_password_check = forms.CharField(max_length=150, required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['new_password', 'new_password_check', ]


class EmailForgot(forms.ModelForm):
    class Meta:
        model = User
        fields =['email']