from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from api.users.users_routes import set_users_routes

v1_router = routers.DefaultRouter(trailing_slash=False)

set_users_routes(v1_router)

urlpatterns = [
    url(r'^v1/', include(v1_router.urls, namespace='v1')),
    url(r'^v1/token', obtain_jwt_token),
]
