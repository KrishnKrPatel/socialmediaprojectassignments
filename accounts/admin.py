from django.contrib import admin
from accounts.models import User
# Register your models here.

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'name']
