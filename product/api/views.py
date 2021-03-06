from django.core.paginator import Paginator
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .serializers import ProductSerializer
from product.models import Product


class ProductPagenation(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'



class ProductAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagenation

