from .views import register_form, user_login, edit_profile, profile, list_users,ChangePasswordView
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView

app_name = 'customer'

urlpatterns = [
    path('register/', register_form, name='register'),
    path('login/', user_login, name='login'),
    path('profile/<int:user_id>', profile, name='profile'),
    # path('change_password/<int:user_id>', change_password, name='change'),
    path('edit/<int:user_id>', edit_profile, name='edit'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('product:home')), name='logout'),
    path('list_users/', list_users, name='list'),
    path('change_password/', ChangePasswordView, name='change_password'),
]
