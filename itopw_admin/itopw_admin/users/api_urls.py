from django.urls import path, include
from rest_framework import routers
from itopw_admin.users.apis import UsersViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'users', UsersViewSet)

app_name = "users"
urlpatterns = [
    path('', include(router.urls)),
]
