from rest_framework.generics import ListAPIView
from accounts.models import User
from accounts.serializers import UserSerializer
from accounts.utils import search


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        search_field = self.request.query_params.get(search, None)
        if search_field:
            if queryset.filter(email__exact=search_field).exists():
                queryset = queryset.filter(email__exact=search_field)
            else:
                queryset = queryset.filter(name__icontains=search_field)
        return queryset

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)