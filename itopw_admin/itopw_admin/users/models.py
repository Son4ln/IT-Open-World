from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, BooleanField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from itopw_admin.utils.models import BaseModel
from itopw_admin.utils.soft_delete import SoftDelete


class User(AbstractUser, BaseModel):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    is_deative = BooleanField(_("Is Deactive"), default=False)
    is_writter = BooleanField(_("Is Writter"), default=False)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    class Meta:
        db_table = "users"
