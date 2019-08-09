from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, BooleanField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from itopw_admin.utils.models import BaseModel


class User(AbstractUser, BaseModel):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    phone = CharField(_("Phone"), blank=True, max_length=20)
    is_writter = BooleanField(_("Writter"), default=False)
    email_notification = BooleanField(_("Email Notification"), default=False)
    web_notification = BooleanField(_("Website Notification"), default=False)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def name_verbose(self):
        return self.name or _("Updating...")

    def active_verbose(self):
        if self.is_active:
            return _('Active')
        return _('Deactive')

    def name_as_avatar(self):
        """
        get first char in name or username to create avatar
        """
        try:
            return self.name[0]
        except IndexError:
            return self.username[0]

    class Meta:
        db_table = "users"
