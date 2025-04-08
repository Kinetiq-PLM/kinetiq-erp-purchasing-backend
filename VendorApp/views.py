from rest_framework import generics
from .models import VendorApplication
from .serializers import VendorApplicationSerializer

class VendorApplicationListView(generics.ListAPIView):
    """Retrieve a list of all vendor applications"""
    queryset = VendorApplication.objects.all()
    serializer_class = VendorApplicationSerializer

class VendorApplicationCreateView(generics.CreateAPIView):
    """Create a new vendor application"""
    queryset = VendorApplication.objects.all()
    serializer_class = VendorApplicationSerializer
