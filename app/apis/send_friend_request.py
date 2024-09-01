from app.apis.serializers import FriendSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SendFriendRequestAPIView(APIView):
    serializer_class = FriendSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(from_user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)