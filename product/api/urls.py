from django.urls import path, include

from .views import ProductAPI


urlpatterns = [
    # url('api/', include(router.urls), name='api'),
    path('', ProductAPI.as_view(), name='Product'),

]
