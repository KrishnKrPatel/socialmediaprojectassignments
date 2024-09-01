from django.urls import path, include
from .user_creation import UserCreateAPIView
from .user_list import UserListAPIView


urlpatterns = [
    path('auth/', include('accounts.apis.authentication.urls')),
    path('auth/signup/', UserCreateAPIView.as_view(), name="user_creation"),
    path('users/', UserListAPIView.as_view(), name="user")
]