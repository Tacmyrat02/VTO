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
import cv2
import numpy as np
import mediapipe as mp
from django.shortcuts import render

mp_pose = mp.solutions.pose
mp_selfie_seg = mp.solutions.selfie_segmentation

def virtual_tryon(request, product_id):
    product = Product.objects.get(pk=product_id)
    
    if request.method == 'POST' and request.FILES.get('image'):
        # Ulanyjynyň suratyny işle
        uploaded_file = request.FILES['image']
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
        
        # 1. Beden ölçeglerini anykla
        with mp_pose.Pose() as pose:
            results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            if results.pose_landmarks:
                height_px = calculate_height(results)  # Özüňiz ýazmaly
                shoulder_px = calculate_shoulder_width(results)  # Özüňiz ýazmaly
        
        # 2. Eşigi bedene oturt
        cloth_img = cv2.imread(product.image.path)
        adjusted_cloth = adjust_cloth_to_body(image, cloth_img, results.pose_landmarks)
        
        # 3. Reňk balansyny düzet
        color_corrected = correct_cloth_color(adjusted_cloth)
        
        # 4. Arka plany aýyr
        with mp_selfie_seg.SelfieSegmentation(model_selection=1) as seg:
            segmented = remove_background(color_corrected)
        
        # 5. Ölçeg maslahat ber
        size_recommendation = recommend_size(height_px, shoulder_px)
        
        context = {
            'product': product,
            'processed_image': segmented,
            'size_recommendation': size_recommendation
        }
        return render(request, 'products/tryon_result.html', context)
    
    return render(request, 'products/virtual_tryon.html', {'product': product})