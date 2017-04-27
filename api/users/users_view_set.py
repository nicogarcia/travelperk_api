from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from api.users.users_model import User
from api.users.users_serializer import UserSerializer


class UsersViewSet(CreateModelMixin,
                   GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
