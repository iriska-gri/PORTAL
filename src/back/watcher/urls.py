from django.urls import path
from .views import *

urlpatterns = [
    path('counter/', Counter.as_view(),name="CountVisitors"),
    path('dataforstatistics/', DataForStatisticsAPIView.as_view(), name="DataForStatistics"),
    path('selectedlinks/', SelectedLinksAPIView.as_view(),name="SelectedLinks")
]