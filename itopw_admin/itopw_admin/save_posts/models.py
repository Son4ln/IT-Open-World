from django.db.models import ForeignKey, CASCADE, Model
from itopw_admin.posts.models import Post
from itopw_admin.users.models import User


class SavePosts(Model):
    """
    User save post to view again
    """
    post = ForeignKey(Post, on_delete=CASCADE)
    user = ForeignKey(User, related_name="post_saved", on_delete=CASCADE)
