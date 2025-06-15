from django.shortcuts import render, get_object_or_404  # Import render here
from .models import Product, Category

def product_list(request):
    categories = Category.objects.prefetch_related('product_set').all()
    return render(request, 'products/list.html', {
        'categories': categories
    })

def product_detail(request, pk):
    product = get_object_or_404(Product.objects.select_related('category'), pk=pk)
    return render(request, 'products/detail.html', {
        'product': product
    })
from django.shortcuts import render, redirect
from .forms import ProductUploadForm

def upload_product(request):
    if request.method == 'POST':
        form = ProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductUploadForm()
    return render(request, 'products/upload.html', {'form': form})