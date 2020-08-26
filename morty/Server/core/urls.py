from django.urls import path, include

from core import views

urlpatterns = [
    path('all_images/', views.all_images, name='all-images'),

    path('single_image/<int:image_id>/', views.single_image, 
        name='single-image'),
]
