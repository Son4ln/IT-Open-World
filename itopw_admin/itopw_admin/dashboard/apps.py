from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DashBoardConfig(AppConfig):
    name = "itopw_admin.dashboard"
    verbose_name = _("Dashboard")
