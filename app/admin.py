from django.contrib import admin
from app.models import Friendship


@admin.register(Friendship)
class FriendshipModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'from_user', 'to_user', 'status', 'created_at', 'updated_at']
