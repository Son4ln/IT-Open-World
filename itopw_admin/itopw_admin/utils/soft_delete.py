from django.db.models import DateTimeField, Manager, Model
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class SoftDeleteManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class TrashManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=False)


class SoftDelete(Model):
    deleted_at = DateTimeField(null=True)

    objects = SoftDeleteManager()
    origin_objects = Manager()
    trash_objects = TrashManager()

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()
