from rest_framework import generics, status
from rest_framework.response import Response
from .models import PurchaseQuotation
from .serializers import PurchaseQuotationSerializer, VendorSerializer
from purchase_quotation.models import Vendor  # Assuming the app name for Vendor is `quotation_quotation`


# List view to get all purchase quotations
class PurchaseQuotationListView(generics.ListAPIView):  # For GET all quotations
    queryset = PurchaseQuotation.objects.all()
    serializer_class = PurchaseQuotationSerializer

# Create view to create a new purchase quotation
class PurchaseQuotationCreateView(generics.CreateAPIView):  # For POST new quotation
    queryset = PurchaseQuotation.objects.all()
    serializer_class = PurchaseQuotationSerializer

class VendorListView(generics.ListAPIView):  # For GET all vendors
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseQuotationDocumentNoListView(generics.ListAPIView):
    """
    View to return a list of document_no values.
    """
    def get_queryset(self):
        """
        Return only the document_no values from PurchaseQuotation.
        """
        return PurchaseQuotation.objects.values_list('document_no', flat=True)

    def list(self, request, *args, **kwargs):
        """
        Override the list method to return a plain list of document_no values.
        """
        queryset = self.get_queryset()
        return Response(queryset)
    

class PurchaseQuotationEditView(generics.UpdateAPIView):
    """
    View to edit an existing PurchaseQuotation.
    """
    queryset = PurchaseQuotation.objects.all()
    serializer_class = PurchaseQuotationSerializer
    lookup_field = 'quotation_id'  # Use 'quotation_id' as the lookup field