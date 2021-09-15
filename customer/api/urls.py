from django.urls import path, include
from .views import RegisterAPI

app_name = 'customer_api'

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
]
