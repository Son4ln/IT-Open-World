from django.contrib.auth import get_user_model
from django.forms import ModelForm, TextInput, EmailInput, CheckboxInput, PasswordInput, CharField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class SuperUpdateUserForm(ModelForm):
    """Form definition for MODELNAME."""
    # Check change password
    password = CharField(
        widget=PasswordInput(attrs={"class": "form-control", "placeholder": _("Current Password")}))
    new_password = CharField(
        widget=PasswordInput(attrs={"class": "form-control", "placeholder": _("New Password")}))
    confirm_password = CharField(
        widget=PasswordInput(attrs={"class": "form-control", "placeholder": _("Confirm Password")}))

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
            "email": EmailInput(attrs={"class": "form-control", "placeholder": _("Your Last Name"), "aria-describedby":"basic-addon1"}),
            "phone": TextInput(attrs={"class": "form-control", "placeholder": _("Your Phone Number"), "aria-describedby":"basic-addon1"}),
            "is_staff": CheckboxInput(),
            "is_superuser": CheckboxInput(),
            "is_writter": CheckboxInput(),
            "email_notification": CheckboxInput(),
            "web_notification": CheckboxInput(),
            "name": TextInput(attrs={"class": "form-control", "placeholder": _("Your Full Name")}),
        }
