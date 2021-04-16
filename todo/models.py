from django.db import models
from django.utils import timezone


class TodoList(models.Model):
    item = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
