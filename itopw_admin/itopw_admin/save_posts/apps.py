from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SavePostsConfig(AppConfig):
    name = "itopw_admin.save_posts"
    verbose_name = _("Save Posts")
