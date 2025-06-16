from django.db import models
from django.core.validators import MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

from django.db import models

class Product(models.Model):
    CLOTHING = 'CL'
    JEWELRY = 'JW'
    TYPE_CHOICES = [
        (CLOTHING, 'Egin-eşik'),
        (JEWELRY, 'Jeweller'),
    ]
    
    # Esasy meýdanlar
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    product_type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=CLOTHING)
    
    # Egin-eşik üçin goşmaça meýdanlar
    size = models.CharField(max_length=10, blank=True, null=True)  # S, M, L, XL
    color = models.CharField(max_length=50, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    
    # Virtual Try-On üçin teklipler
    recommended_height = models.CharField(max_length=50, blank=True, null=True)  # "160-175cm"
    recommended_shoulder = models.CharField(max_length=50, blank=True, null=True)  # "38-42cm"