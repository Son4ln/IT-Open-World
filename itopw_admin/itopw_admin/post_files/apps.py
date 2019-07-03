from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PostFilesConfig(AppConfig):
    name = "itopw_admin.post_files"
    verbose_name = _("Post Files")
