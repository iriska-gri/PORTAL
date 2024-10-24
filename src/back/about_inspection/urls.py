from django.urls import path
from .views import *



urlpatterns = [
    path('getfactsize/', GetFactSize.as_view(), name='getfactsize'),
    path('getstatesize/', GetStateSize.as_view(), name='getstatesize'),
    path('getinspectiondirections/', GetInspectionDirections.as_view(), name='getinspectiondirections'),
    path('getstructure/', GetStructure.as_view(), name='getstructure'),
    path('getvacancy/', GetVacancies.as_view(), name='getvacancy'),
    path('postresponsevacancy/', PostResponseVacancies.as_view(), name='postresponsevacancy'),
    
    
]