from django.urls import path
from .send_friend_request import SendFriendRequestAPIView
from .accept_friend_requests import AcceptFriendRequestAPIView
from .reject_friend_request import RejectFriendRequestAPIView
from .all_friendship_list import FriendshipListAPIView

urlpatterns = [
    path('send/', SendFriendRequestAPIView.as_view(), name="send_friend_request"),
    path('list/', FriendshipListAPIView.as_view(), name="friend_list"),
    path('accept/<int:pk>/', AcceptFriendRequestAPIView.as_view(), name="accept_friend_request"),
    path('reject/<int:pk>/', RejectFriendRequestAPIView.as_view(), name="reject_friend_request"),
]