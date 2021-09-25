from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView

from order.views import CustomerOrderDetailView, AddToCartView, MyCartView, ManageCartView, EmptyCartView, CheckoutView
app_name = 'order'

urlpatterns = [
    path("profile/order-<int:pk>/", CustomerOrderDetailView.as_view(),
         name="customerorderdetail"),
    path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
    path("my-cart/", MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/", ManageCartView.as_view(), name="managecart"),
    path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
]
