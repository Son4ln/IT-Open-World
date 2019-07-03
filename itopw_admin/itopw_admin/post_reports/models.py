from django.db.models import ForeignKey, CASCADE, Model, TextField
from django.utils.translation import ugettext_lazy as _
from itopw_admin.posts.models import Post
from itopw_admin.users.models import User


class PostReport(Model):
    post = ForeignKey(Post, related_name="reports", on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)
    content = TextField(_("Report Content"), null=False, blank=False)
