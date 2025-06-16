from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:product_id>/try-on/', views.virtual_tryon, name='virtual_tryon'),
    path('upload/', views.upload_product, name='upload_product'),  # New line
]
