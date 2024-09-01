from django.urls import path
from .token_generation import (TokenGeneratorView,
                               RefreshTokenView,
                               VerifyTokenView)
urlpatterns = [
    path("login/", TokenGeneratorView.as_view(),
         name="generate-jwt-token"),
    path("refresh/", RefreshTokenView.as_view(), name="jwt-refresh-token"),
    path("verify/", VerifyTokenView.as_view(), name="jwt-verify-refresh")
]
