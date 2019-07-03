from django.db.models import ForeignKey, CASCADE, Model, TextField, CharField
from django.utils.translation import ugettext_lazy as _
from itopw_admin.users.models import User


class Notification(Model):
    user = ForeignKey(User, related_name="notification", on_delete=CASCADE)
    content = TextField(_("Content"), null=False, blank=False)
    url = CharField(_("Url"), null=False, blank=False, max_length=500)
