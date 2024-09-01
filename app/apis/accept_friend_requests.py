from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from app.apis.serializers import FriendSerializer
from app.models import Friendship
from app.choices import ACCEPTED_CHOICE_STATUS, PENDING_CHOICE_STATUS


class AcceptFriendRequestAPIView(generics.UpdateAPIView):
    serializer_class = FriendSerializer
    queryset = Friendship.objects.all()

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status == PENDING_CHOICE_STATUS:
            instance.status = ACCEPTED_CHOICE_STATUS
            instance.save()
        return Response(self.serializer_class(instance).data, status=status.HTTP_200_OK)