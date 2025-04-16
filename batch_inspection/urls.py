# inspection/urls.py
from django.urls import path
from .views import InspectionCreateView, InspectionListView

urlpatterns = [
    path('create/', InspectionCreateView.as_view(), name='inspection-create'),
    path('list/', InspectionListView.as_view(), name='inspection-list'),
]
