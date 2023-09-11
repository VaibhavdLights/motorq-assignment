from django.urls import path
from .signup_view import user_signup
from .login_view import user_login
from .views import user_list

urlpatterns = [
    path('signup/', user_signup, name='user-signup'),
    path('login/', user_login, name='user-login'),
    path('users/', user_list, name='user-list'),
]
