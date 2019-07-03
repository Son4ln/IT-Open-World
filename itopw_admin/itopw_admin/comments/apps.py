from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommentsConfig(AppConfig):
    name = "itopw_admin.comments"
    verbose_name = _("Comments")
