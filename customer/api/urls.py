from django.urls import path, include
from django.conf.urls import url
from .views import RegisterAPI, ChangeCustomerPassword


urlpatterns = [
    # url('api/', include(router.urls), name='api'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('customer_change_password', ChangeCustomerPassword.as_view(), name='customer_change_password'),
    # path('customer_change_password/', ChangePasswordView.as_view(), name='change_password_api'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

