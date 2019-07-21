from django.core.paginator import Paginator
from django.db.models import Q

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated

from itopw_admin.users.serializers import UserSerializer
from itopw_admin.users.models import User
from itopw_admin.utils.response import response_200, response_403


class UsersViewSet(ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """
        api to get list users and draw to datatables
        """
        if request.GET.get('search[value]'):
            # Search item
            self.queryset = User.objects.filter(
                Q(username__icontains=request.GET.get('search[value]')) |
                Q(name__icontains=request.GET.get('search[value]')) |
                Q(email__icontains=request.GET.get('search[value]')))

        if request.GET.get('order[0][dir]') == 'desc':
            self.queryset = self.queryset.order_by('-id')

        # count users record
        total_record = self.queryset.count()
        paginator = Paginator(self.queryset, request.GET.get('length', 0))
        paginator_list = paginator.get_page(int(request.GET.get('start', 0)) + 1)
        serializer = self.get_serializer(paginator_list, many=True)
        response = {
            "draw": request.GET.get('draw', 0),
            "recordsTotal": total_record,
            "recordsFiltered": total_record,
            'data': serializer.data
        }

        return response_200(response)

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            instance = self.get_object()
            instance.is_active = request.data['is_active']
            instance.save()
            serializer = self.get_serializer(instance)
            return response_200(serializer.data)
        else:
            return response_403()
