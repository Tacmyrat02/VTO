from django import forms
from .models import Product

class ProductUploadForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'image', 'product_type']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }