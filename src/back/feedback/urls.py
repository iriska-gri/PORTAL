from django.urls import path
from .views import *


urlpatterns = [
   path('feedbackdata/', FeedbackAPIView.as_view(), name='feedbackdata'),
 

]