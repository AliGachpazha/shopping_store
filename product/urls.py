from .views import HomeView, AllProductsView, ProductDetailView,search
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView

app_name = 'product'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("all-products/", AllProductsView.as_view(), name="allproducts"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="productdetail"),
    path("search/", search, name="search"),
]
