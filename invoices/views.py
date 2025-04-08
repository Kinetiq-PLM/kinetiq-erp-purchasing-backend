from rest_framework import generics
from .models import APInvoice
from .serializers import APInvoiceSerializer

class APInvoiceListView(generics.ListAPIView):
    queryset = APInvoice.objects.all()
    serializer_class = APInvoiceSerializer
