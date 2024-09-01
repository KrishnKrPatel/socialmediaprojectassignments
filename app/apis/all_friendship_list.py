from rest_framework import generics
from app.choices import ACCEPTED_CHOICE_STATUS
from app.apis.serializers import FriendSerializer
from app.models import Friendship


# listing all the friend list related to a particular user

class FriendshipListAPIView(generics.ListAPIView):
    serializer_class = FriendSerializer
    queryset = Friendship.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(from_user=self.request.user,
                                       status=ACCEPTED_CHOICE_STATUS)

        return queryset

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
