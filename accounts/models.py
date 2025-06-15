from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    body_measurements = models.JSONField(blank=True, null=True)  # Beden ölçegleri
# accounts/models.py
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField()  # Boý (sm)
    shoulder_width = models.FloatField()  # Egin ini (sm)
    waist = models.FloatField()  # Bel (sm)