from django.urls import path
from itopw_admin.users.views import (
    ListUser,
    UpdateUser
)

app_name = "users"
urlpatterns = [
    path("", ListUser.as_view(), name="list_user"),
    path("update/<int:pk>/", view=UpdateUser.as_view(), name="update"),
]
