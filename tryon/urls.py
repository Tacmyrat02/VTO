from django.urls import path
from . import views

urlpatterns = [
    path('', views.tryon_home, name='tryon_home'),  # Baş sahypa
    path('webcam/', views.webcam_tryon, name='webcam_tryon'),
    path('upload/', views.upload_tryon, name='upload_tryon'),
]