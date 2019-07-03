from django.db.models import CharField, ImageField, SlugField, Model, ForeignKey, CASCADE
from django.utils.translation import ugettext_lazy as _
from itopw_admin.utils.models import AbstractModel
from itopw_admin.posts.models import Post


class Category(AbstractModel):
    avatar = ImageField(
        _("Avatar"), upload_to=None, height_field=500, width_field=500, max_length=500, null=False, blank=False)
    name = CharField(_("Title"), null=False, blank=False, max_length=500, unique=True)
    slug = SlugField(_("Slug"), max_length=500, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class PostCategories(Model):
    category = ForeignKey(Category, related_name="posts", on_delete=CASCADE)
    post = ForeignKey(Post, related_name="categories", on_delete=CASCADE)
