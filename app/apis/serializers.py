from rest_framework import serializers
from app.models import Friendship


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['id', 'from_user', 'to_user', 'status', 'created_at', 'updated_at']

        extra_kwargs = {
            'status': {
                'read_only': True
            },
            'from_user': {
                'read_only': True
            },
            'created_on': {
                'read_only': True
            },
            'updated_on': {
                'read_only': True
            },
        }


class UpdateFriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['status']