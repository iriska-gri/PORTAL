from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

urlpatterns = [
    
    path('links/', LinkAPIView.as_view(), name='LinkAPIView'),

    path('gallery/', GalleryAPIView.as_view(), name='GalleryAPIView'),
    path('carousels/', CarouselsAPIView.as_view(), name='CarouselsAPIView'),
    path('screensaver/', ScreensaverAPIView.as_view(), name='ScreensaverAPIView'),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('newscrossroad/', NewsCrossroadAPIView.as_view(), name='NewsCrossroadAPIView')
    
 
    
]