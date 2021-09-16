from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username,phone, email, first_name, last_name, user_type, password=None):
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

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,phone, email, first_name, last_name, user_type, password=None):
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


class Address(models.Model):
    address = models.CharField(max_length=400, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
