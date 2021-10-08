from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer
from rest_framework.views import APIView
from product.models import Product
import copy
from rest_framework import generics

from .serializers import ProductSerializer
from product.models import Product


class ProductAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductAPI(generics.ListAPIView):
#     def get(self, request, _id=None):
#         products = None
#         page_size = 3
#         if _id:
#             products = ProductSerializer(get_object_or_404(Product, pk=_id)).data
#         else:
#             # getting all serialized products
#             products = ProductSerializer(Product.objects.all(), many=True).data
#             paginated_products = []
#             products_in_page = []
#             for product in products:
#                 if len(products_in_page) < page_size:
#                     products_in_page.append(product)
#                 if len(products_in_page) == page_size:
#                     paginated_products.append(copy.copy(products_in_page))
#                     products_in_page.clear()
#             paginated_products.append(copy.copy(products_in_page))
#             products = paginated_products
#         return Response(products)
