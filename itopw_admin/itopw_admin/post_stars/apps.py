from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PostStarsConfig(AppConfig):
    name = "itopw_admin.post_stars"
    verbose_name = _("Post Stars")
