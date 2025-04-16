from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import APInvoice, ExternalModule, DocumentItems
from .serializers import APInvoiceSerializer, ExternalModuleSerializer, DocumentItemsSerializer

class APInvoiceListView(generics.ListAPIView):
    queryset = APInvoice.objects.all()
    serializer_class = APInvoiceSerializer

# List view for ExternalModule
class ExternalModuleListView(generics.ListAPIView):
    queryset = ExternalModule.objects.all()
    serializer_class = ExternalModuleSerializer

# List view for DocumentItems
class DocumentItemsListView(generics.ListAPIView):
    queryset = DocumentItems.objects.all()
    serializer_class = DocumentItemsSerializer

# Create view for APInvoice
class APInvoiceCreateView(generics.CreateAPIView):
    """
    API view to create a new APInvoice.
    """
    queryset = APInvoice.objects.all()
    serializer_class = APInvoiceSerializer
