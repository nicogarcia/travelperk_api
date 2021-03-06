from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils import timezone

from api.users.users_manager import UserManager


class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'

    created_at = models.DateTimeField(default=timezone.now)

    email = models.EmailField(unique=True)

    objects = UserManager()

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email
