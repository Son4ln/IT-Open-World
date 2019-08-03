from django.contrib.auth import get_user_model
from django.forms import ModelForm, TextInput, EmailInput
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class SuperUpdateUserForm(ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'is_staff', 'is_superuser', 'is_writter', 'phone',
            'email_notification', 'web_notification', 'name')

        widgets = {
            "first_name": TextInput(attrs={"class": "form-control", "placeholder": _("Your First Name")}),
            "last_name": TextInput(attrs={"class": "form-control", "placeholder": _("Your Last Name")}),
            "name": TextInput(attrs={"class": "form-control", "placeholder": _("Your Full Name")}),
        }
