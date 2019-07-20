from rest_framework.serializers import ModelSerializer
from itopw_admin.users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'deactive_verbose', 'name_as_avatar']
