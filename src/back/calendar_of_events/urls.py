from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

urlpatterns = [
    # path('calendarEvents/', CalendarEventsAPIView.as_view(), name='calendarEvents'),
    path('get_employees/', GetEmployees.as_view(), name='get_employees'),
    path('my_calendars/', MyCalendars.as_view(), name='get_calendars'),
    path('exclusion_dates/', ExclusionDatesAPIView.as_view(), name='exclusion_dates'),
    path('my_events/', MyEvents.as_view(), name='myvents')
    # path('createEvents/', CreateEventsAPIView.as_view(), name='createEvents')
]
