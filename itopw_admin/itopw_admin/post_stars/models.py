from django.db.models import ForeignKey, CASCADE, Model
from itopw_admin.posts.models import Post
from itopw_admin.users.models import User


class PostStars(Model):
    post = ForeignKey(Post, related_name="stars", on_delete=CASCADE)
    user = ForeignKey(User, related_name="post_stars", on_delete=CASCADE)
