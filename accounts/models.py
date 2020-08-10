from django.conf import settings
from django.db import models


class Profile(models.Model):
    image = models.ImageField(upload_to='accounts/')
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
