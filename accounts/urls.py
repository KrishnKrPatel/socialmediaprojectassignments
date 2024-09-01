from django.urls import path, include

urlpatterns = [
    path('', include('accounts.apis.urls')),
]