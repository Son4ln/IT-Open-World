from django.urls import path
from itopw_admin.users.views import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
    ListUser,
    UpdateUser
)

app_name = "users"
urlpatterns = [
    path("", ListUser.as_view(), name="list_user"),
    path("update/<int:pk>/", view=UpdateUser.as_view(), name="update"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
