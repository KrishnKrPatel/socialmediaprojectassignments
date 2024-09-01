from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Friendship(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='sent_requests',
        on_delete=models.CASCADE,
        db_column="from_user_field",
        verbose_name=_("From User")
    )
    to_user = models.ForeignKey(
        User,
        related_name='received_requests',
        on_delete=models.CASCADE,
        db_column="to_user_field",
        verbose_name=_("To User")
    )
    status = models.CharField(
        _('Status'),
        max_length=10,
        choices=[
            ('pending', 'Pending'),
            ('accepted', 'Accepted'),
            ('rejected', 'Rejected')
        ],
        default='pending',
        db_column="status_field"
    )
    created_at = models.DateTimeField(
        _('Created at'),
        db_column="created_at_field",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('Updated at'),
        db_column="updated_at_field",
        auto_now=True
    )

    class Meta:
        unique_together = ('from_user', 'to_user')
        db_table = "friendship"

    def __str__(self):
        return f"{self.from_user.email} -> {self.to_user.email} ({self.status})"
