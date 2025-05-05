from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import APInvoice, DocumentHeader
from .serializers import APInvoiceSerializer, DocumentHeaderSerializer

class APInvoiceListView(generics.ListAPIView):
    queryset = APInvoice.objects.all()
    serializer_class = APInvoiceSerializer


# List view for DocumentItems
class DocumentHeaderListView(generics.ListAPIView):
    queryset = DocumentHeader.objects.all()
    serializer_class = DocumentHeaderSerializer

# Create view for APInvoice
class APInvoiceCreateView(generics.CreateAPIView):
    """
    API view to create a new APInvoice.
    """
    queryset = APInvoice.objects.all()
    serializer_class = APInvoiceSerializer
