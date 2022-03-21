from django.urls import path
from .views import *

urlpatterns = [
    path('',Homeview.as_view(),name='home'),
    path('condidate<int:id>/',CondidateView.as_view(),name='condidate'),
    path('delete<int:id>/',Deletecondidate.as_view(),name='delete'),
]
