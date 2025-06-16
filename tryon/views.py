from django.shortcuts import render  # Add this import
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import cv2
import numpy as np
import base64
import mediapipe as mp

# Initialize MediaPipe models
mp_pose = mp.solutions.pose
mp_selfie_segmentation = mp.solutions.selfie_segmentation

def tryon_home(request):
    """Virtual Try-On home page view"""
    return render(request, 'tryon/home.html')
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/detail.html', {'product': product})
@csrf_exempt
def upload_tryon(request):
    if request.method == 'POST' and request.FILES.get('image'):
        try:
            # Get uploaded image
            uploaded_file = request.FILES['image']
            product_id = request.POST.get('product_id', 1)  # Default product
            
            # Convert InMemoryUploadedFile to OpenCV format
            img = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
            
            # Process image (example: face detection)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            
            # Draw rectangles on faces (for demo)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            
            # Convert back to base64 for web display
            _, buffer = cv2.imencode('.jpg', img)
            processed_image = base64.b64encode(buffer).decode('utf-8')
            
            return JsonResponse({
                'status': 'success',
                'processed_image': f'data:image/jpeg;base64,{processed_image}'
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return render(request, 'tryon/upload.html')

@csrf_exempt
def webcam_tryon(request):
    if request.method == 'POST':
        try:
            # Webcam görnüşini işle
            image_data = request.POST.get('image').split(',')[1]  # Base64 kodlanan surat
            nparr = np.frombuffer(base64.b64decode(image_data), np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            # MediaPipe bilen beden deteksiýasy
            with mp_pose.Pose() as pose:
                results = pose.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                if results.pose_landmarks:
                    # Netijäni JSON-a öwür
                    landmarks = [{'x': lm.x, 'y': lm.y} for lm in results.pose_landmarks.landmark]
                    return JsonResponse({'status': 'success', 'landmarks': landmarks})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return render(request, 'tryon/webcam.html')