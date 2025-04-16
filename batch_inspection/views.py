# inspection/views.py
from rest_framework import generics
from .models import Inspection
from .serializers import InspectionSerializer

class InspectionCreateView(generics.CreateAPIView):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer

class InspectionListView(generics.ListAPIView):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer
