from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from app.apis.serializers import FriendSerializer
from app.models import Friendship
from app.choices import PENDING_CHOICE_STATUS, REJECTED_CHOICE_STATUS


class RejectFriendRequestAPIView(generics.UpdateAPIView):
    serializer_class = FriendSerializer
    queryset = Friendship.objects.all()

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status == PENDING_CHOICE_STATUS:
            instance.status = REJECTED_CHOICE_STATUS
            instance.save()
        return Response(self.serializer_class(instance).data, status=status.HTTP_200_OK)