from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView
)

urlpatterns = [
    
    path('links/', CaorusAPIView.as_view(), name='CaorusAPIView'),

    
]