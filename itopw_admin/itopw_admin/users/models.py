from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, BooleanField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from itopw_admin.utils.models import BaseModel


class User(AbstractUser, BaseModel):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    is_deative = BooleanField(_("Is Deactive"), default=False)
    is_writter = BooleanField(_("Is Writter"), default=False)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def deactive_verbose(self):
        if self.is_deative:
            return _('Deactive')
        return _('Active')

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
