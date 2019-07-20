from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from users.serializers import UserSerializer
from itopw_admin.users.models import User


class UsersViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
