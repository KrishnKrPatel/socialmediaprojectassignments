from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from django.db import models
import uuid

# Create your models here.


class User(AbstractBaseUser):
    """
        User data model to store user information.
    """
    id = models.UUIDField(primary_key=True, db_column='id',
                          default=uuid.uuid4, editable=False)
    name = models.CharField(_('Name'), db_column='name_field',
                                  max_length=30, null=True, blank=True)
    email = models.EmailField(_('Email Address'), db_column='user_email',
                              max_length=254, db_index=True, unique=True)

    is_active = models.BooleanField(
        _("Is Active"), default=True, db_column='active_status', )
    is_staff = models.BooleanField(
        _("Is Staff"), default=False, db_column='staff_status', )

    is_superuser = models.BooleanField(
        _("Is SuperUser"), default=False, db_column='super_user', )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`"
        return True

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
