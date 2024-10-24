from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

urlpatterns = [
    path('', SafetyAPIView.as_view()),
    path('gettypes/', SafetyTypeAPIView.as_view(), name="SafetyTypeAPIView"),
#     path('files/', SafetyFileAPIView.as_view(), name='safety_files'),
#     path('responsibility/', SafetyResponsebilityAPIView.as_view(), name='responsibility'),
#     path('committee_files/', CommitteeFilesAPIView.as_view(), name='committee_files')
]