from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import json

class User(AbstractUser):
    # Profile fields
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    body_measurements = models.JSONField(
        default=dict,
        blank=True,
        help_text="JSON of user's body measurements (height, shoulder, waist, etc.)"
    )
    
    # Fix auth model clashes
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name="vto_user_groups",  # Unique related_name
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name="vto_user_permissions",  # Unique related_name
        related_query_name="user",
    )

    def __str__(self):
        return f"{self.username} (VTO User)"
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    height = models.FloatField(help_text="Height in cm") 
    shoulder_width = models.FloatField(help_text="Shoulder width in cm")
    waist = models.FloatField(help_text="Waist in cm")
    # Add other measurements as needed

    def get_measurements_json(self):
        return json.dumps({
            'height': self.height,
            'shoulder': self.shoulder_width,
            'waist': self.waist
        })