from django.db import models


# Create your models here.
class Storage(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    access_key_id = models.CharField(max_length=255)
    secret_access_key = models.CharField(max_length=255)
    region = models.CharField(max_length=255)

