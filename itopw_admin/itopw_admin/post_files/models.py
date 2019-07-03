from django.db.models import CharField, ForeignKey, CASCADE, FileField, IntegerField, Model
from django.utils.translation import ugettext_lazy as _
from itopw_admin.posts.models import Post


class PostFiles(Model):
    file = FileField(_("File Url"), upload_to=None, max_length=500, null=True, blank=True)
    name = CharField(_("Title"), null=False, blank=False, max_length=500, unique=True)
    # file size as byte
    size = IntegerField(_("File Size"), null=False, default=0)
    mime = CharField(_("File Mime"), null=False, max_length=10)
    post = ForeignKey(Post, related_name="files", verbose_name=_("Post Files"), on_delete=CASCADE)

    def __str__(self):
        return self.name
