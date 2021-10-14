import secrets ,string
from random import random

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token



class CustomUserManager(BaseUserManager):
    def create_user(self, username, phone, email, first_name, last_name, user_type, password=None, password1=None,
                    password2=None):
        if not email:
            raise ValueError('Students must have email')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            type=user_type,
            phone=phone,
            username=username,
        )

        user.set_password(password, password1, password2, )
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone, email, first_name, last_name, user_type, password=None):
        if not email:
            raise ValueError('Students must have email')
        user = self.model(email=self.normalize_email(email),
                          first_name=first_name,
                          last_name=last_name,
                          user_type=user_type,
                          phone=phone,
                          username=username,
                          )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    phone_regex = RegexValidator(regex=r'^9\d{9}$',
                                 message="شماره تماس باید با فرمت ۹۱۲۷۸۹۳۴۵۶ وارد شود")
    username = models.CharField(verbose_name='username', max_length=60, unique=True)
    phone = models.CharField(validators=[phone_regex], max_length=10, unique=True)
    address = models.CharField(max_length=400, blank=True)
    city = models.CharField(max_length=400, blank=True)
    post_code = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    CUSTOMER = 'customer'
    MANAGER = 'manager'
    EMPLOYEE = 'employee'
    USER_TYPE_CHOICES = [
        (MANAGER, 'مدیر'),
        (CUSTOMER, 'مشتری'),
        (EMPLOYEE, 'کارمند'),
    ]
    user_type = models.CharField(max_length=600, choices=USER_TYPE_CHOICES, default=CUSTOMER, null=False, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name', 'user_type']
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_token(self):
        token = Token.objects.get(user=self)
        return token.key


    def save(self, *args, **kwargs):
        if self.user_type == User.MANAGER:
            self.promoteUserToAdmin()
        elif self.user_type == User.EMPLOYEE:
            self.promoteUserToDepartmentAdmin()
        super(User, self).save(*args, **kwargs)

    def promoteUserToAdmin(self):
        self.is_superuser = True
        self.is_staff = True
        self.is_admin = True

    def promoteUserToDepartmentAdmin(self):
        self.is_staff = True




@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'),
                                                   reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
