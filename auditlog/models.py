from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from users.models import Group

# Create your models here.

class AuditLogModel(models.Model):

    class Action(models.TextChoices):
        CREATE = 'ADD'
        EDIT = 'EDT'
        DELETE = 'DEL'
        

    file_name = models.CharField(max_length=255)
    action = models.CharField(choices=Action.choices, max_length=3)
    user = models.ManyToManyField(User)
    datestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    group = models.ManyToManyField(Group)
    comment = models.CharField(max_length=60, null=True)