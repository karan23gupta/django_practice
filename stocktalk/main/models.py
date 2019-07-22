from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class myusers(models.Model):
    stock = models.CharField(max_length=100)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.stock
