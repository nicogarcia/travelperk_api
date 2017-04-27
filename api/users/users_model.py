from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'

    email = models.EmailField(unique=True)

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email
