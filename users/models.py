# users/models.py
import random
import uuid

from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from api.models import Storage


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True)
    access_layer = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class File(models.Model):
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_busy = models.BooleanField(default=False)


class Group(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    members = models.ManyToManyField(User, related_name='group_member')
    files = models.ManyToManyField(File)

    tariff_level = models.IntegerField(default=None, null=True, blank=True)
    tariff_exp = models.DateField(default=None, null=True, blank=True)
    volume = models.IntegerField(default=0, null=True, blank=True)

