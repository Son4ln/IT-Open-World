from django.db.models import TextField, ForeignKey, CASCADE
from django.utils.translation import ugettext_lazy as _
from itopw_admin.utils.models import BaseModel
from itopw_admin.users.models import User
from itopw_admin.posts.models import Post
from itopw_admin.utils.soft_delete import SoftDelete


class Comment(SoftDelete ,BaseModel):
    content = TextField(_("Content"), null=False, blank=False)
    user = ForeignKey(User, related_name="comments", verbose_name=_("User Comments"), on_delete=CASCADE)
    post = ForeignKey(Post, related_name="comments", verbose_name=_("Post Comments"), on_delete=CASCADE)
    parent = ForeignKey("Comment", related_name="reply", verbose_name=_("Reply"), on_delete=CASCADE)
