from django.urls import path
from .views import *


urlpatterns = [
   path('generalvacation/', GeneralVacationAPIView.as_view(), name='generalvacation'),
   path('dailyroundup/', DailyRoundUpAPIView.as_view(), name='dailyroundup'),
   path('dailyload/', DailyloadAPIView.as_view(), name='dailyload'),

]