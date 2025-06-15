from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import MinValueValidator

class User(AbstractUser):
    # Profile Image
    avatar = models.ImageField(
        upload_to='user_avatars/',
        null=True,
        blank=True,
        help_text="Upload a clear front-facing photo for better virtual try-on results"
    )
    
    # Body Measurements (in cm)
    height = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(100)],
        help_text="Height in centimeters"
    )
    shoulder_width = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(30)],
        help_text="Shoulder width in centimeters"
    )
    waist = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(50)],
        help_text="Waist circumference in centimeters"
    )
    
    # Fix auth model conflicts
    groups = models.ManyToManyField(
        Group,
        related_name="vto_users",
        related_query_name="vto_user",
        blank=True,
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="vto_users",
        related_query_name="vto_user",
        blank=True,
        verbose_name='user permissions'
    )

    def get_body_data(self):
        """Returns measurements as dict for AR processing"""
        return {
            'height': self.height,
            'shoulder': self.shoulder_width,
            'waist': self.waist,
            'gender': 'male'  # Can be made into a model field
        }

    def __str__(self):
        return f"{self.username} ({self.email})"