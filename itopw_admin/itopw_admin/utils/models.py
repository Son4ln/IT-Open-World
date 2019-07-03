# from django.contrib.auth import get_user_model
from django.db.models import DateTimeField, ForeignKey, Model, CASCADE
from django.conf import settings


class AbstractModel(Model):
    created_at = DateTimeField(auto_now_add=True, null=True)
    updated_at = DateTimeField(auto_now=True, null=True)
    creator = ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='%(app_label)s_%(class)s_creator',
        null=True,
        blank=True,
        on_delete=CASCADE
    )
    last_modified_by = ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='%(app_label)s_%(class)s_last_modified',
        null=True,
        blank=True,
        on_delete=CASCADE
    )

    class Meta:
        abstract = True
