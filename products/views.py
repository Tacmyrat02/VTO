from django.shortcuts import get_object_or_404
from .models import Product, Category

def product_list(request):
    categories = Category.objects.prefetch_related('product_set').all()
    return render(request, 'products/list.html', {'categories': categories})

def product_detail(request, pk):
    product = get_object_or_404(Product.objects.select_related('category'), pk=pk)
    return render(request, 'products/detail.html', {'product': product})