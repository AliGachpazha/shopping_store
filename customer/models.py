from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)


class Management(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Address(models.Model):
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=30)
