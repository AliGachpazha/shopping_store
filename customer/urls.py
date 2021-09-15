from .views import register_form, user_login, Home, edit_profile, profile
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView

app_name = 'customer'

urlpatterns = [
    path('', Home, name='home'),
    path('register/', register_form, name='register'),
    path('login/', user_login, name='login'),
    path('profile/<int:user_id>', profile, name='profile'),
    path('edit/<int:user_id>', edit_profile, name='edit'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('customer:home')), name='logout'),
]
