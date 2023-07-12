from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class User(AbstractUser):
    qrecord = models.IntegerField(default=0)



