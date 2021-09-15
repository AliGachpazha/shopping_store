from django.urls import path, include

app_name = 'core_api'

urlpatterns = [
    path('customer/', include('customer.api.urls')),

]
