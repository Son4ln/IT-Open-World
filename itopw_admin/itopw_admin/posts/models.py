from django.db.models import CharField, ImageField, SlugField, TextField, ForeignKey, CASCADE
from django.utils.translation import ugettext_lazy as _
from itopw_admin.utils.models import BaseModel
from itopw_admin.users.models import User
from itopw_admin.series.models import Series
from itopw_admin.utils.soft_delete import SoftDelete


class Post(SoftDelete ,BaseModel):

    STATUS_1 = "WT"
    STATUS_2 = "AC"
    STATUS_3 = "DN"
    STATUS_4 = "CL"
    STATUS_5 = "ACL"

    STATUS_CHOICES = (
        (STATUS_1, _("Waiting")),
        (STATUS_2, _("Accept")),
        (STATUS_3, _("Deny")),
        (STATUS_4, _("Close")),
        (STATUS_5, _("Admin close")),
    )

    avatar = ImageField(
        _("Avatar"), upload_to=None, height_field=500, width_field=500, max_length=500, null=False, blank=False)
    title = CharField(_("Title"), null=False, blank=False, max_length=500, unique=True)
    slug = SlugField(_("Slug"), max_length=500, null=False, blank=False, unique=True)
    content = TextField(_("Content"), null=False, blank=False)
    links = TextField(_("Links"), null=False, blank=False)
    origin = CharField(_("Origin"), null=False, blank=False, max_length=500)
    status = CharField(_("Status"), null=False, max_length=3, choices=STATUS_CHOICES, default=STATUS_1)
    user = ForeignKey(User, related_name="posts", verbose_name=_("Post Owner"), on_delete=CASCADE)
    series = ForeignKey(Series, related_name="posts", on_delete=CASCADE)

    def __str__(self):
        return self.title
