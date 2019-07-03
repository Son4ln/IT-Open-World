from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SeriesConfig(AppConfig):
    name = "itopw_admin.series"
    verbose_name = _("Series")
