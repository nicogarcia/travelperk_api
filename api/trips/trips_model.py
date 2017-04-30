from django.db import models
from django.db.models import Model
from django.utils import timezone

from api.users.users_model import User


class Trip(Model):
    created_at = models.DateTimeField(default=timezone.now)

    name = models.CharField(max_length=50, blank=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
