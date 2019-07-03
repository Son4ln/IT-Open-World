from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NotificationConfig(AppConfig):
    name = "itopw_admin.notification"
    verbose_name = _("Notification")
