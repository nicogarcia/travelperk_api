from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from api.users.users_manager import UserManager


class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'

    email = models.EmailField(unique=True)

    objects = UserManager()

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email
