from django.db import models
from django.core.validators import MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    CLOTHING = 'CL'
    JEWELRY = 'JW'
    TYPE_CHOICES = [
        (CLOTHING, 'Clothing'),
        (JEWELRY, 'Jewelry'),
    ]
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    model_3d = models.FileField(upload_to='3d_models/', blank=True, null=True)
    product_type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.get_product_type_display()})"