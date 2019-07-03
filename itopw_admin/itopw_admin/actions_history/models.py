from django.db.models import ForeignKey, CASCADE, Model, CharField
from django.utils.translation import ugettext_lazy as _
from itopw_admin.users.models import User


class ActionsHistory(Model):
    ACTION_1 = "AC"  # accep post
    ACTION_2 = "DN"  # Deny post
    ACTION_3 = "ACL"   # Addmin close post
    ACTION_4 = "INS"  # Thêm
    ACTION_5 = "DEL"  # Xóa
    ACTION_6 = "UPD"  # Sửa
    ACTION_7 = "DEA"  # Deactive account

    ACTION_ICONS = (
        (ACTION_1, "fa fa-check-circle"),
        (ACTION_2, "fa fa-backspace"),
        (ACTION_3, "fa fa-ban"),
        (ACTION_4, "fa fa-file-import"),
        (ACTION_5, "fa fa-trashe"),
        (ACTION_6, "fa fa-user-edit"),
        (ACTION_7, "fa fa-user-slash"),
    )

    user = ForeignKey(User, related_name="actions_history", on_delete=CASCADE)

    # icon of action
    # may be fontawesome
    action = CharField(_("Action"), choices=ACTION_ICONS, null=False, max_length=3)
    content = CharField(_("Content"), null=False, blank=False, max_length=500)
    url = CharField(_("Content"), null=False, blank=False, max_length=500)
