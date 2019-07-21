from rest_framework.serializers import ModelSerializer
from itopw_admin.users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name_verbose', 'username', 'email', 'is_active', 'active_verbose', 'name_as_avatar']
